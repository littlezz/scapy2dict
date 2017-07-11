# scapy2pickle
Scapy packet to pickle

Usage
-----

```python
from scapy.all import sniff
from scapy2pickle import to_pickle
pkt = sniff(count=1)[0]

# pickle dummps
data = to_pickle(pkt)
```
