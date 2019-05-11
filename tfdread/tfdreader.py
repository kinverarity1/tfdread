from datetime import datetime
import json

import click

from tfdread.binary_utils import *


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

        f.seek(self.index_b["i2"] + 138)
        self.index_c = IndexC().unpack(f)

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

        self.timestamp = datetime(
            *[self.timestamp_field["date"][i] for i in (0, 1, 3, 4, 5, 6)]
        )

    def to_dict(self, debug=False):
        result = {
            "_filename": self.filename,
            "timestamp": self.timestamp,
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

    def to_json(self, indent=2, **kwargs):
        d = self.to_dict()
        d["timestamp"] = str(d["timestamp"])
        return json.dumps(d, default=lambda o: o.odict(), indent=indent, **kwargs)


@click.command()
@click.argument("f", type=click.Path(exists=True))
@click.option("-d", "--debug", default=False)
def open_entry_point(f, debug):
    with TFD(f) as f2:
        print(f2.to_json(debug=debug))
