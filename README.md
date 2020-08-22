# Morton3D ([Homepage](https://pypi.org/project/Morton3D/1.0/))
Efficient pythonic implementation of 3D Morton encoding and decoing.

### Installation

pip install:
```shell script
pip install Morton3D==1.0
```
install from source:
```shell script
git clone https://github.com/Jianningli/Morton3D
cd Morton3D
python setup.py install
```

### Usage

```python
import Morton3D
m=Morton3D.zorder(9) # 9 is the bit length
mortonValue,mortonBinary=m.Morton(51,20,50) # encoding, (51,20,50) is the 3D integer coordinate.
coordinate=m.deMorton(192681,0) # decoding, given the mortonValue, return the 3D coordinate
# decoding, given the morton value in bit representation, return the 3D coordinate, 1 is the flag.
coordinate=m.deMorton('000000000101111000010101001',1)
```

* [1] [Z-order Curve](https://en.wikipedia.org/wiki/Z-order_curve)
* [2] [Uploading Python Pagecage to PyPi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)
