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
    ('北海道余市郡余市町朝日町', ('北海道', '余市郡余市町')),
    ('宮城県仙台市泉区市名坂字東裏97-1', ('宮城県', '仙台市泉区')),
    ('奈良県高市郡高取町', ('奈良県', '高市郡高取町')),
    ('北海道余市郡余市町黒川町', ('北海道', '余市郡余市町')),
    ('東京都', ('東京都', '')),
    ('台東区', ('', '')),
]


@pytest.mark.parametrize('address, expect', test_data)
def test_separate_japanese_addresses(address, expect):
    prefecture, city = expect
    parsed_address = separate_address(address)
    assert parsed_address.prefecture == prefecture
    assert parsed_address.city == city
