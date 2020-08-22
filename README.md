# Morton3D
Efficient pythonic implementation of 3D Morton encoding and decoing (https://en.wikipedia.org/wiki/Z-order_curve).

```
import Morton3D
m=Morton3D.zorder(9) # 9 is the bit length
mortonValue,mortonBinary=m.Morton(51,20,50) # encoding (51,20,50) is the 3D integer coordinate.
coordinate=m.deMorton(192681,0) # decoding, given the mortonValue, return the 3D coordinate
# decoding, given the morton value in bit representation (mortonBinary), return the 3D coordinate, 1 is the flag.
coordinate=m.deMorton('000000000101111000010101001',1)
```
