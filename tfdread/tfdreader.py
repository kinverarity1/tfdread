import json

import click

from tfdread.binary_utils import *


class IndexA(Record):
    fields = [("i1", "short", "2h", 1, lambda v: v)]


class IndexADate(Record):
    fields = [("date", "short", "12s", 1, lambda v: str(v))]


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
        fields=[("contents", "", "{:d}s".format(length), 1, lambda v: v.decode("ascii"))]
    ).unpack(file)

    return {
        "IndexA": indexA,
        "IndexADate": indexADate,
        "IndexB": indexB,
        "IndexC": indexC,
        "InfoA": infoA,
    }
