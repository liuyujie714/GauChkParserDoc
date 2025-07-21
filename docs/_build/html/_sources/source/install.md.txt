# Introduction

A Gaussian `.chk` parser to extract basic information. All energy values are in `Hartree`, length values are in `Angstrom`.  Gaussian `09` and `16` x64 version of Linux and Windows is OK.



```{warning}
<font color=red>No warranty</font> is provided for the correctness of this program. If you observe inconsistencies or anomalies during use, please submit an issue on my [github](https://github.com/liuyujie714/GauChkParserDoc/issues).
```



# Installation

```
pip install GauChkParser -i https://test.pypi.org/simple/
```

Please Always install the **Latest** version

```{note}
Currently Only supported on Linux and Windows with Python >= 3.8
```



# Example

```python
from GauChkParser import ChkReader

obj = ChkReader("yourjob.chk")
mol = obj.params.mol

print(f'Route: {obj.params.route}')
print(f'Natoms: {mol.natoms}')
print(f'Total charge: {mol.totchg}')
print(f'Multiplicity {mol.multiplicity}')
print(f'Element names: {mol.names}')
print(f'Coords (Angstrom): {mol.coords}')
print(f'Hessian Matrix: {mol.hessian}')
print(f'Cell size: {mol.cell}')

# write gjf file
obj.write_gjf("XXX.gjf")

```

