import os.path

from climate.utils import slugify


def test_slugify_with_special_chars():
    """Test slugify() with punctuation marks"""

    text = 'France (Europe)'
    expected = 'france-europe'
    assert slugify(text) == expected


def test_slugify_with_unicode_chars():
    """Test slugify() with unicode chars"""

    text = 'Åland'
    expected = 'aland'
    assert slugify(text) == expected
