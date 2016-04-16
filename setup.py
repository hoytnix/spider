#!/usr/bin/env python

"""Setup script for spider."""

import setuptools

from spider import __project__, __version__

try:
    README = open("readme.md").read()
    CHANGES = open("changes.md").read()
except IOError:
    DESCRIPTION = "<placeholder>"
else:
    DESCRIPTION = README + '\n' + CHANGES

setuptools.setup(
    name=__project__,
    version=__version__,

    description="Spider for analyzing the web.",
    url='https://github.com/pr0xmeh/anavah-spider',
    author='Michael Hoyt',
    author_email='mike@anavah.co',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=(DESCRIPTION),
    classifiers=[
        # TODO: update this list to match your application: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Environment :: Amazon Web Services',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],

    install_requires=open("requirements.txt").readlines(),
)
