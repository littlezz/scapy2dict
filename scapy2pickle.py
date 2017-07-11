from scapy.packet import NoPayload
import pickle
from collections import OrderedDict

__all__ = ['to_pickle', 'Packet2Pickle']


def to_pickle(pkt):
    return Packet2Pickle(pkt).to_pickle()




class Packet2Pickle:
    def __init__(self, pkt):
        self.pkt = pkt


    @staticmethod
    def _layer2dict(obj):
        d = {}
        for f in obj.fields_desc:
            value = getattr(obj, f.name)
            d[f.name] = value
        return {obj.name:d}


    def _to_dict(self):
        d = OrderedDict()
        pkt = self.pkt
        while True:
            d.update(self._layer2dict(pkt))
            if isinstance(pkt.payload, NoPayload):
                break
            else:
                pkt = pkt.payload
        return d



    def to_pickle(self):
        d = self._to_dict()
        return pickle.dumps(d)



