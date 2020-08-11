"""Awesome package."""
import logging
import re

from dataclasses import dataclass

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()

logger.addHandler(handler)

logger.setLevel(logging.INFO)

__prefecture_rule = '京都府|.+?[都道府県]'
__prefecture_pattern = re.compile(__prefecture_rule)
__address_prefecture = re.compile(
    '(京都府|.+?[都道府県])(.+郡)?(.+?[市町村])?(.+?区)?(.*)', re.UNICODE)


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
        ParsedAddress(prefecture='北海道', city='')
        >>> separate_address('奈良県高市郡高取町')
        ParsedAddress(prefecture='奈良県', city='')
    """
    address = address.strip()
    parsed_address = ParsedAddress()

    if len(address) == 0:
        return parsed_address

    matched_prefecture = __prefecture_pattern.match(address)
    if not matched_prefecture:
        return parsed_address

    prefecture = matched_prefecture.group()
    # remove a string of matching prefectures
    address = address.replace(prefecture, '')
    parsed_address.prefecture = prefecture

    return parsed_address