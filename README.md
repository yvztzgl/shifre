# shifre
Shifre is a Python password generator.
This library creates highly secure password with randomness and pure Python.

You can generate passwords like this:
```text
2X3i;6Z364dMR0v7SViyafwBx8>,20xybH232;Zp69875i!7LL")cN2F5rh^h
?r018u91>J0hEld6(NMC1Xot7el!ojh)7ualOxP
%Y85Ibq}:aEVjX0'6$C)>8>6L_7Abb#5+;Dvxi0-Le"
```

### Installation
```sh
$ pip install shifre
```

### Usage
```python
import shifre
# Character count, digit count, symbol count and allow upper case
# returns a string password
password = shifre.generatePassword(64,10,15,True)
```