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

How to use it in combination with pandas.

```python
import pandas as pd
from japanese_addresses import separate_address

df = pd.read_csv('sample.csv')
df.head()
"""
	address
0	宮城県仙台市泉区市名坂字東裏97-1
1	鹿児島県志布志市志布志町志布志
2	東京都　神津島村２８４番
"""
target_col = 'address'

# https://stackoverflow.com/questions/16236684/apply-pandas-function-to-column-to-create-multiple-new-columns
def get_separate_address(address):
    parsed_address = separate_address(address)
    return parsed_address.prefecture, parsed_address.city, parsed_address.street


df['prefecture'], df['city'], df['street']= zip(*df[target_col].map(get_separate_address))
df.head()
"""
	address	prefecture	city	street
0	宮城県仙台市泉区市名坂字東裏97-1	宮城県	仙台市泉区	市名坂
1	鹿児島県志布志市志布志町志布志	鹿児島県	志布志市	志布志町志布志
2	東京都　神津島村２８４番	東京都	神津島村
"""
```

## Testing

```
pip install poetry
poetry install
poetry run pytest
```

## License
Japanese_addresses are licensed under [MIT](https://github.com/wakamezake/japanese-addresses/blob/master/LICENSE)

### [prefecture2city2street.pkl](https://github.com/wakamezake/japanese-addresses/blob/master/japanese_addresses/prefecture2city2street.pkl)

[prefecture2city2street.pkl](https://github.com/wakamezake/japanese-addresses/blob/master/japanese_addresses/prefecture2city2street.pkl) is a derivative work with a modification of [geolonia
/
japanese-addresses](https://github.com/geolonia/japanese-addresses)

Also, [prefecture2city2street.pkl](https://github.com/wakamezake/japanese-addresses/blob/master/japanese_addresses/prefecture2city2street.pkl) was created using [csv_to_dict.py](https://github.com/wakamezake/japanese-addresses/blob/master/scripts/csv_to_dict.py)

### Information on the original work

[![geolonia/japanese-addresses - GitHub](https://gh-card.dev/repos/geolonia/japanese-addresses.svg)](https://github.com/geolonia/japanese-addresses)

https://geolonia.github.io/japanese-addresses/

### タイトル
Geolonia 住所データ

### 出典
本データは、以下のデータを元に、毎月 Geolonia にて更新作業を行っています。
- [国土交通省位置参照情報ダウンロードサイト](https://nlftp.mlit.go.jp/cgi-bin/isj/dls/_choose_method.cgi)
- [郵便番号データダウンロード - 日本郵便](https://www.post.japanpost.jp/zipcode/download.html)

### スポンサー
[一般社団法人 不動産テック協会](https://retechjapan.org/)

### ライセンス
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja)
