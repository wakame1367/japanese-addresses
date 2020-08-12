import pytest
from dataclasses import is_dataclass

from japanese_addresses import separate_address, ParsedAddress


def is_dataclass_instance(obj):
    return is_dataclass(obj) and not isinstance(obj, type)


def is_default_value(parsed_address: ParsedAddress):
    assert parsed_address.prefecture == ''
    assert parsed_address.city == ''


def test_separate_address():
    parsed_address = separate_address('')
    assert is_dataclass_instance(parsed_address)
    is_default_value(parsed_address)

    # TODO: detect with invalid value
    parsed_address = separate_address('京東都')
    assert is_dataclass_instance(parsed_address)


test_data = [
    ('鹿児島県志布志市志布志町志布志', ('鹿児島県', '志布志市', '志布志町志布志')),
    ('奈良県高市郡高取町大字兵庫', ('奈良県', '高市郡高取町', '大字兵庫')),
    ('山形県西村山郡河北町大字岩木山口', ('山形県', '西村山郡河北町', '大字岩木')),
    ('佐賀県杵島郡大町町大字大町上大町', ('佐賀県', '杵島郡大町町', '大字大町')),
    ('北海道余市郡余市町朝日町', ('北海道', '余市郡余市町', '朝日町')),
    ('宮城県仙台市泉区市名坂字東裏97-1', ('宮城県', '仙台市泉区', '市名坂')),
    ('奈良県高市郡高取町', ('奈良県', '高市郡高取町', '')),
    ('北海道余市郡余市町黒川町', ('北海道', '余市郡余市町', '黒川町')),
    ('石川県野々市市', ('石川県', '野々市市', '')),
    ('岐阜県山県市', ('岐阜県', '山県市', '')),
    ('岐阜県郡上市', ('岐阜県', '郡上市', '')),
    ('千葉県市川市', ('千葉県', '市川市', '')),
    ('東京都', ('東京都', '', '')),
    ('台東区', ('', '', '')),
]


@pytest.mark.parametrize('address, expect', test_data)
def test_separate_japanese_addresses(address, expect):
    prefecture, city, street = expect
    parsed_address = separate_address(address)
    assert parsed_address.prefecture == prefecture
    assert parsed_address.city == city
    assert parsed_address.street == street
