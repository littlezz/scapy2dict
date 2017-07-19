# scapy2dict
Scapy packet to dict


install
-------
`pip3 install scapy2dict`  


Usage
-----

```python
from scapy.all import sniff
from scapy2dict import to_dict
pkt = sniff(count=1)[0]

# To ChainMap dict
data = to_dict(pkt)

# to exactly dict
data = to_dict(pkt, strict=True)
```
