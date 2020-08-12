"""Awesome package."""
import logging
import pickle
import re
from pathlib import Path
from kanjize import int2kanji
from dataclasses import dataclass

DIR_PATH = Path(__file__).parent
pkl_name = 'prefecture2city2street.pkl'
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()

logger.addHandler(handler)

logger.setLevel(logging.INFO)

with open(str(DIR_PATH / pkl_name), 'rb') as f:
    prefecture2city = pickle.load(f)

__number_pat = re.compile(r'(\d+)')


@dataclass
class ParsedAddress:
    prefecture: str = ''
    city: str = ''
    street: str = ''


def number2kansuji(number_in_string: str) -> str:
    """

    Args:
        number_in_string:

    Returns:
    Example:
        >>> number2kansuji('北1条西12丁目')
        '北一条西十二丁目'
        >>> number2kansuji('北１条西１２丁目')
        '北一条西十二丁目'
    """
    number_in_string_sub = number_in_string
    for match in __number_pat.finditer(number_in_string):
        number = match.group()
        kansuji = int2kanji(int(number))
        split_string = list(number_in_string_sub)
        split_string[match.start():match.end()] = kansuji
        number_in_string_sub = ''.join(split_string)
    return number_in_string_sub


def _search(address: str, key2value: dict):
    matched = False
    for key in key2value.keys():
        matched = address.startswith(key)
        if matched:
            break
    return key, matched


def separate_address(address: str) -> ParsedAddress:
    """

    Args:
        address:

    Returns:

    Example:
        >>> separate_address('北海道札幌市中央区北1条西2丁目')
        ParsedAddress(prefecture='北海道', city='札幌市中央区', street='北一条西二丁目')
        >>> separate_address('奈良県高市郡高取町')
        ParsedAddress(prefecture='奈良県', city='高市郡高取町', street='')
    """
    address = address.strip()
    address = number2kansuji(address)
    parsed_address = ParsedAddress()

    if len(address) == 0:
        return parsed_address

    prefecture, matched_prefecture = _search(address, prefecture2city)
    # not found
    if not matched_prefecture:
        return parsed_address

    city2street = prefecture2city.get(prefecture)

    # remove a string of matching prefectures
    address = address.replace(prefecture, '')
    parsed_address.prefecture = prefecture

    city, matched_city = _search(address, city2street)
    # not found
    if not matched_city:
        return parsed_address

    streets = city2street.get(city)

    # remove a string of matching cities
    address = address.replace(city, '')
    parsed_address.city = city

    if len(address) == 0:
        return parsed_address

    matched_street = False
    for street in streets:
        matched_street = address.startswith(street)
        if matched_street:
            break

    # not found
    if not matched_street:
        return parsed_address

    # remove a string of matching cities
    address = address.replace(street, '')
    parsed_address.street = street

    return parsed_address
