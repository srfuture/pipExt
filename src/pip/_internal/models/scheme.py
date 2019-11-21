"""
For types associated with installation schemes.

For a general overview of available schemes and their context, see
https://docs.python.org/3/install/index.html#alternate-installation.
"""

from pip._internal.utils.models import Base


class Scheme(Base):
    """A Scheme holds paths which are used as the base directories for
    artifacts associated with a Python package.
    """

    __slots__ = ['platlib', 'purelib', 'headers', 'scripts', 'data']

    def __init__(
        self,
        platlib,  # type: str
        purelib,  # type: str
        headers,  # type: str
        scripts,  # type: str
        data,  # type: str
    ):
        self.platlib = platlib
        self.purelib = purelib
        self.headers = headers
        self.scripts = scripts
        self.data = data
