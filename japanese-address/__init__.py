"""Awesome package."""
import logging
import re
from collections import namedtuple

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()

logger.addHandler(handler)

logger.setLevel(logging.INFO)

__prefecture_rule = '京都府|.+?[都道府県]'
__prefecture_pattern = re.compile(__prefecture_rule)
__address_prefecture = re.compile(
    '(京都府|.+?[都道府県])(.+郡)?(.+?[市町村])?(.+?区)?(.*)', re.UNICODE)

# TODO: use dataclass
ParsedAddress = namedtuple('parsed_address', ['prefecture', 'city'])


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
        parsed_address(prefecture='北海道', city='')
        >>> separate_address('奈良県高市郡高取町')
        parsed_address(prefecture='奈良県', city='')
    """
    address = address.strip()
    prefecture = ''
    city = ''

    if len(address) == 0:
        return ParsedAddress(prefecture, city)

    matched_prefecture = __prefecture_pattern.match(address)
    if not matched_prefecture:
        return ParsedAddress(prefecture, city)

    prefecture = matched_prefecture.group()
    # remove a string of matching prefectures
    address = address.replace(prefecture, '')

    return ParsedAddress(prefecture, city)
