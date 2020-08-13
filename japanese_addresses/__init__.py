"""Awesome package."""
import logging
import pickle
import re
from pathlib import Path
from typing import Iterable
from dataclasses import dataclass
from kanjize import int2kanji

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


def _search(address: str, search_target: Iterable) -> str:
    matched_length = 0
    matched_key = ''
    # longest match
    for key in search_target:
        matched = address.startswith(key)
        if matched and (len(key) > matched_length):
            matched_key = key
            matched_length = len(key)
    return matched_key


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

    prefecture = _search(address, prefecture2city.keys())
    # not found
    if not prefecture:
        return parsed_address

    city2street = prefecture2city.get(prefecture)

    # remove a string of matching prefectures
    address = address.replace(prefecture, '')
    address = address.strip()
    parsed_address.prefecture = prefecture

    if len(address) == 0:
        return parsed_address

    city = _search(address, city2street.keys())
    # not found
    if not city:
        return parsed_address

    streets = city2street.get(city)

    # remove a string of matching cities
    address = address.replace(city, '')
    address = address.strip()
    parsed_address.city = city

    if len(address) == 0:
        return parsed_address

    street = _search(address, streets)

    # not found
    if not street:
        return parsed_address

    # remove a string of matching cities
    address = address.replace(street, '')
    address = address.strip()
    parsed_address.street = street

    return parsed_address
