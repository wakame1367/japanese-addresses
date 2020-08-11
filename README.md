# japanese-addresses

[![Python package](https://github.com/wakamezake/japanese-addresses/workflows/Python%20package/badge.svg?branch=master)](https://github.com/wakamezake/japanese-addresses/actions?query=workflow%3A%22Python+package%22)
[![codecov](https://codecov.io/gh/wakamezake/japanese-addresses/branch/master/graph/badge.svg)](https://codecov.io/gh/wakamezake/japanese-addresses)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/wakamezake/japanese-addresses/master)

Parsing Japan addresses to prefectures and cities.

## Installation

```
pip install git+https://github.com/wakamezake/japanese-addresses.git
```

## Examples

```python
from japanese_addresses import separate_address

parsed_address = separate_address('宮城県仙台市泉区市名坂字東裏97-1')

print(parsed_address)
"""
ParsedAddress(prefecture='宮城県', city='')
"""
```

## Testing

```
pip install poetry
poetry install
poetry run pytest
```
