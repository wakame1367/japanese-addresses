"""Awesome package."""
import logging
import pickle
from pathlib import Path

from dataclasses import dataclass

DIR_PATH = Path(__file__).parent
pkl_name = 'prefecture2city2street.pkl'
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()

logger.addHandler(handler)

logger.setLevel(logging.INFO)

with open(str(DIR_PATH / pkl_name), 'rb') as f:
    prefecture2city = pickle.load(f)


@dataclass
class ParsedAddress:
    prefecture: str = ''
    city: str = ''
    street: str = ''


def separate_address(address: str) -> ParsedAddress:
    """

    Args:
        address:

    Returns:

    Example:
        >>> separate_address('北海道札幌市中央区北1条西2丁目')
        ParsedAddress(prefecture='北海道', city='札幌市中央区', street='北一条西十二丁目')
        >>> separate_address('奈良県高市郡高取町')
        ParsedAddress(prefecture='奈良県', city='高市郡高取町', street='')
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

    city2street = prefecture2city.get(prefecture)

    # remove a string of matching prefectures
    address = address.replace(prefecture, '')
    parsed_address.prefecture = prefecture

    matched_city = False
    for city in city2street.keys():
        matched_city = address.startswith(city)
        if matched_city:
            break
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
