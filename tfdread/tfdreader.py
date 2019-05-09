import json

import click

from tfdread.binary_utils import *


format_index_a_date = lambda *args: "{}-{:02.0f}-{:02.0f} {:02.0f}:{:02.0f}:{:02.0f}".format(
    args[0], args[1] + args[2], args[3], args[4], args[5], args[6]
)


class IndexA(Record):
    fields = [("i1", "short", "2h", 1, lambda v: v)]


class IndexADate(Record):
    fields = [("date", "short", "12h", 12, lambda *v: str(list(zip(range(len(v)), v))))]
    # fields = [("date", "short", "12h", 12, format_index_a_date)]


class IndexB(Record):
    fields = [("i2", "short", "2h", 1, lambda v: v)]


class IndexC(Record):
    fields = [("l", "short", "2h", 1, lambda v: v)]




@click.command()
@click.argument("file", type=click.File("rb"))
def read(file):
    print(json.dumps(read_file(file), indent=2, default=lambda o: o.odict()))


def read_file(file):
    indexA = IndexA().unpack(file)

    file.seek(42)
    indexADate = IndexADate().unpack(file)

    file.seek(indexA["i1"] + 8)
    indexB = IndexB().unpack(file)

    file.seek(indexB["i2"] + 138)
    indexC = IndexC().unpack(file)

    file.seek(116)
    length = indexA["i1"] - 116
    infoA = Record(
        fields=[
            ("contents", "", "{:d}s".format(length), 1, lambda v: v.decode("ascii").split("\r\n"))
        ]
    ).unpack(file)

    return {
        "IndexA": indexA,
        "IndexADate": indexADate,
        "IndexB": indexB,
        "IndexC": indexC,
        "InfoA": infoA,
    }
