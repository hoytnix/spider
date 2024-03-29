"""Package for Spider."""

import sys

__project__ = 'spider'
__version__ = '0.0.0'

VERSION = "{0} v{1}".format(__project__, __version__)

PYTHON_VERSION = 3, 5

if sys.version_info < PYTHON_VERSION:  # pragma: no cover (manual test)
    sys.exit("Python {}.{}+ is required.".format(*PYTHON_VERSION))

try:
    # pylint: disable=wrong-import-position
    import sys
except ImportError:
    pass
