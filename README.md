# python-package-template

[![Python package](https://github.com/wakamezake/japanese-address/workflows/Python%20package/badge.svg?branch=master)](https://github.com/wakamezake/python-package-template/actions?query=workflow%3A%22Python+package%22)
[![codecov](https://codecov.io/gh/wakamezake/japanese-address/branch/master/graph/badge.svg)](https://codecov.io/gh/wakamezake/python-package-template)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/wakamezake/japanese-address/master)

Parsing Japan addresses to prefectures and cities.

## Installation

```
pip install git+https://github.com/wakamezake/japanese-address.git
```

## Examples

```python
from japanese_address import separate_address

parsed_address = separate_address('宮城県仙台市泉区市名坂字東裏97-1')

print(parsed_address)
"""
parsed_address(prefecture='宮城県', city='')
"""
```

## Testing

```
pip install poetry
poetry install
poetry run pytest
```
