from datetime import datetime
import json
import logging
import re

import click

from tfdread.binary_utils import *


logger = logging.getLogger(__name__)


class IndexA(Record):
    fields = [("i1", "short", "2h", 1, lambda v: v)]


class IndexADate(Record):
    fields = [("date", "short", "12h", 12, lambda *v: v)]


class IndexB(Record):
    fields = [("i2", "short", "2h", 1, lambda v: v)]


class IndexC(Record):
    fields = [("l", "short", "2h", 1, lambda v: v)]


class TFD:
    """Open TFD file.

    Args:
        f (filename or file object): TFD file

    """

    def __init__(self, f):
        self.f = f

    def __enter__(self):
        try:
            self.f.seek(1)
        except AttributeError:
            self.filename = self.f
            self.f = open(self.filename, "rb")
        else:
            self.filename = None
            self.f.seek(0)
        self.read()
        return self

    def __exit__(self, *args):
        self.f.close()

    def read(self):
        f = self.f
        f.seek(0)

        self.index_a = IndexA().unpack(f)
        f.seek(42)
        self.timestamp_field = IndexADate().unpack(f)

        f.seek(self.index_a["i1"] + 8)
        self.index_b = IndexB().unpack(f)

        index_c_loc = self.index_b["i2"] + 138
        f.seek(index_c_loc)
        self.index_c = IndexC().unpack(f)
        l = self.index_c["l"]
        self.data_pkg_loc = index_c_loc + 150

        f.seek(116)
        length = self.index_a["i1"] - 116
        self.info_a = Record(
            fields=[
                (
                    "contents",
                    "",
                    "{:d}s".format(length),
                    1,
                    lambda v: v.decode("ascii", errors="ignore").split("\r\n"),
                )
            ]
        ).unpack(f)
        self.info_a_contents = unpack_header_contents(self.info_a["contents"])

        self.timestamp = datetime(
            *[self.timestamp_field["date"][i] for i in (0, 1, 3, 4, 5, 6)]
        )

        dtype_map = {
            "dword": ,
            "word": ,
            "short": ,
            "byte": ,
            "WORD": ,
            "BYTE": ,
        }
        ch_dtypes = [ch["DataType"] for ch in self.channels if "DataType" in ch]
        dtypes = [dtype_map[k] for k in ch_dtypes]

        f.seek(self.data_pkg_loc)
        self.data = []
        while True:
            chunk = f.read(l)
            if len(chunk) < l:
                break
            else:
                self.data.append(str(chunk))
        self.data_shape = len(self.data)

    @property
    def header(self):
        return {k: v for k, v in self.info_a_contents.items() if not re.match(r"Ch\d*", k)}

    @property
    def channels(self):
        return {k: v for k, v in self.info_a_contents.items() if re.match(r"Ch\d*", k)}

    def to_dict(self, debug=False):
        result = {
            "_filename": self.filename,
            "timestamp": self.timestamp,
            "header": self.header,
            "channels": self.channels,
            "data.shape": self.data_shape,
            "data": self.data,
            "_structs": {
                "index_a": self.index_a,
                "timestamp_field": self.timestamp_field,
                "index_b": self.index_b,
                "index_c": self.index_c,
                "info_a": self.info_a,
            },
        }
        if not debug:
            result = {k: v for k, v in result.items() if not k[0] == "_"}
        return result

    def to_json(self, indent=2, debug=False, **kwargs):
        d = self.to_dict(debug=debug)
        d["timestamp"] = str(d["timestamp"])
        return json.dumps(d, default=lambda o: o.odict(), indent=indent, **kwargs)


def unpack_header_contents(hlines):
    """Convert list of lines from the header "InfoA" section to a dictionary.

    Args:
        hlines (list): list of strings

    Returns: dictionary

    """
    sections = {}
    section_name = None
    outside_section = {}
    section = {}
    for i, line in enumerate(hlines):
        logger.debug(line)
        key = re.match(r"\[(.*)\]", line)
        if key:
            section_name = key.group(1)
            continue
        else:
            if not line:
                if section_name:
                    sections[section_name] = section
                    section_name = None
                section = {}
                continue
            else:
                if "=" in line:
                    key, value = [v.strip() for v in line.split("=")]
                    if "," in value:
                        value = value.split(",")
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            value = str(value)
                    if value == "no":
                        value = False
                    if value == "yes":
                        value = True

                    section[key] = value
                else:
                    outside_section[i] = line
    sections["_outside"] = outside_section
    return sections


@click.command()
@click.argument("f", type=click.Path(exists=True))
@click.option("--debug/--no-debug", default=False)
@click.option("--verbose/--quiet", default=False)
def open_entry_point(f, debug, verbose):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    with TFD(f) as f2:
        print(f2.to_json(debug=debug))
