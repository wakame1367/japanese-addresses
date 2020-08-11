from dataclasses import is_dataclass

from japanese_address import separate_address, ParsedAddress


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

