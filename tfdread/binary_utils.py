import collections
import json
import struct


char_array_to_str = lambda length, array: "".join(array)


def debug(*args):
    print(args)
    return str(args)


class Record(struct.Struct):
    def __init__(self, fields=None):
        if not fields is None:
            self.fields = fields
        super(Record, self).__init__(self.fmt)


    def unpack(self, buffer, offset=0):
        _ = buffer.read(offset)
        buffer_extract = buffer.read(self.size)
        self.unpack_items = super(Record, self).unpack(buffer_extract)
        return self

    def odict(self):
        names = []
        values = []
        j = 0
        for i, field in enumerate(self.fields):
            key, description, py_format, k, pformat_func = field
            items = self.unpack_items[j : j + k]
            j += k
            value = pformat_func(*items)
            if isinstance(value, bytes):
                value = value.decode("ascii")
            names.append(key)
            values.append(value)
        return collections.OrderedDict(zip(names, values))

    def __str__(self):
        return json.dumps(
            {
                "super": super(Record, self).__str__(),
                "__class__": str(self.__class__),
                "data": self.odict(),
            },
            indent=2,
        )

    def __getitem__(self, key):
        if key in self.field_names:
            return self.odict()[key]

    @property
    def fmt(self):
        return "=" + "".join([f[2] for f in self.fields])

    @property
    def field_names(self):
        return [f[0] for f in self.fields]
