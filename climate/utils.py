import re
from unicodedata import normalize


def slugify(text):
    """Generate an ASCII-only slug.
    Taken from this gist:
    https://gist.github.com/gergelypolonkai/1866fd363f75f4da5f86103952e387f6
    """
    _punctuation_re = re.compile(
        r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+'
    )

    result = []
    for word in _punctuation_re.split(text.lower()):
        word = normalize(
            'NFKD', word
        ).encode(
            'ascii', 'ignore'
        ).decode(
            'utf-8'
        )

        if word:
            result.append(word)

    return '-'.join(result)
