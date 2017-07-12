from scapy.packet import NoPayload
from collections import OrderedDict


__all__ = ['to_dict', 'Packet2Dict']

__version__ = '0.9'


def to_dict(pkt):
    return Packet2Dict(pkt).to_dict()


class Packet2Dict:
    def __init__(self, pkt):
        self.pkt = pkt


    @staticmethod
    def _layer2dict(obj):
        d = {}
        for f in obj.fields_desc:
            value = getattr(obj, f.name)
            d[f.name] = value
        return {obj.name:d}


    def to_dict(self):
        d = OrderedDict()
        pkt = self.pkt
        while True:
            d.update(self._layer2dict(pkt))
            if isinstance(pkt.payload, NoPayload):
                break
            else:
                pkt = pkt.payload
        return d



