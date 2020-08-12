# japanese-addresses

[![PyPI version](https://badge.fury.io/py/japanese-addresses.svg)](https://badge.fury.io/py/japanese-addresses)
[![Python package](https://github.com/wakamezake/japanese-addresses/workflows/Python%20package/badge.svg?branch=master)](https://github.com/wakamezake/japanese-addresses/actions?query=workflow%3A%22Python+package%22)
[![codecov](https://codecov.io/gh/wakamezake/japanese-addresses/branch/master/graph/badge.svg)](https://codecov.io/gh/wakamezake/japanese-addresses)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/wakamezake/japanese-addresses/master)

Parsing Japan addresses to prefectures and cities.

## Installation

```
pip install japanese-addresses
```

## Examples

```python
from japanese_addresses import separate_address

parsed_address = separate_address('宮城県仙台市泉区市名坂字東裏97-1')

print(parsed_address)
"""
ParsedAddress(prefecture='宮城県', city='仙台市泉区', street='市名坂')
"""

parsed_address = separate_address('鹿児島県志布志市志布志町志布志')

print(parsed_address)
"""
ParsedAddress(prefecture='鹿児島県', city='志布志市', street='志布志町志布志')
"""
```

## Testing

```
pip install poetry
poetry install
poetry run pytest
```

## License
japanese_addresses is licensed under [MIT](https://github.com/wakamezake/japanese-addresses/blob/master/LICENSE)
