import os
import sys

from new_listings_scraper import get_announcement

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def test_latest_announcement():
    assert get_announcement()
