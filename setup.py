"""
Setup and installation for the package.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = """
Simple Python library for interacting with the SmartyStreets API
"""


setup(
    name="smartystreets",
    version="0.1",
    url="http://github.com/chriscohoat/smartystreets",
    author="Chris Cohoat",
    author_email="chris.cohoat@gmail.com",
    keywords=['smartystreets', 'mapquest', 'geocoding', 'google maps', 'geocode'],
    description="An easy-to-use SmartyStreets Geocoding API wrapper.",
    long_description=long_description,
    packages=[
        'smartystreets',
    ],
    install_requires=[
        'requests',
        'ujson',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
