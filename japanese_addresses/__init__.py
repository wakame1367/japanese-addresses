"""Awesome package."""
import logging
import pickle
import re
from pathlib import Path

from dataclasses import dataclass

DIR_PATH = Path(__file__).parent
pkl_name = 'prefecture2city2street.pkl'
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()

logger.addHandler(handler)

logger.setLevel(logging.INFO)

__prefecture_rule = '京都府|.+?[都道府県]'
__city_rule = '(.+郡)?(.+?[市町村])?(.+?区)?'
__prefecture_pattern = re.compile(__prefecture_rule)
__city_pattern = re.compile(__city_rule)
__address_prefecture = re.compile(
    '(京都府|.+?[都道府県])(.+郡)?(.+?[市町村])?(.+?区)?(.*)', re.UNICODE)

with open(str(DIR_PATH / pkl_name), 'rb') as f:
    prefecture2city = pickle.load(f)


@dataclass
class ParsedAddress:
    prefecture: str = ''
    city: str = ''


def is_prefecture(address: str):
    """
    Returns whether the string is a prefecture

    Args:
        address (str):

    Returns:
        bool: whether the string is a prefecture

    Example:
        >>> is_prefecture('京都府')
        True
        >>> is_prefecture('北海道')
        True
    """
    match_obj = __prefecture_pattern.match(address)
    if match_obj:
        return True
    else:
        return False


def separate_address(address: str) -> ParsedAddress:
    """

    Args:
        address:

    Returns:

    Example:
        >>> separate_address('北海道札幌市中央区北1条西2丁目')
        ParsedAddress(prefecture='北海道', city='札幌市中央区')
        >>> separate_address('奈良県高市郡高取町')
        ParsedAddress(prefecture='奈良県', city='高市郡高取町')
    """
    address = address.strip()
    parsed_address = ParsedAddress()

    if len(address) == 0:
        return parsed_address

    matched_prefecture = False
    for prefecture in prefecture2city.keys():
        matched_prefecture = address.startswith(prefecture)
        if matched_prefecture:
            break
    # not found
    if not matched_prefecture:
        return parsed_address

    cities = prefecture2city.get(prefecture)

    # remove a string of matching prefectures
    address = address.replace(prefecture, '')
    parsed_address.prefecture = prefecture

    matched_city = False
    for city in cities.keys():
        matched_city = address.startswith(city)
        if matched_city:
            break
    # not found
    if not matched_city:
        return parsed_address

    # remove a string of matching cities
    address = address.replace(city, '')
    parsed_address.city = city

    return parsed_address
