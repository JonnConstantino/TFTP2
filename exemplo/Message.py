# automatically generated by the FlatBuffers compiler, do not modify

# namespace: exemplo

import flatbuffers

class Message(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMessage(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Message()
        x.Init(buf, n + offset)
        return x

    # Message
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Message
    def Data(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def MessageStart(builder): builder.StartObject(1)
def MessageAddData(builder, data): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0)
def MessageEnd(builder): return builder.EndObject()