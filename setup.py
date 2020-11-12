from setuptools import setup, find_packages
from os import path

#------------------------------------------------------------------------------
# The current standard for setup info.
# For details, see:
#  https://packaging.python.org/guides/distributing-packages-using-setuptools/
#  https://github.com/pypa/sampleproject/blob/master/setup.py
#  https://pypi.org/classifiers/
#  https://choosealicense.com/
#------------------------------------------------------------------------------

def readme():
    # Get the long description from the README file
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()

setup(
    name             = 'mt4pycon',
    # For test uploads, use: X.YaN, X.Y.devN, or X.Y.postN
    version          = '1.0.2',
    author           = 'eabase',
    # author_email can be ignored for provacy
    #author_email     = 'eabase@users.noreply.github.com',
    description      = 'A python script using the mtapi EA on MT4 to get candle data',
    long_description = 'This is an example client using the MT4 API (mtapi) to connect to the MT4 EA, using either an TCP/IP or a pipe port.',
    long_description_content_type='text/plain',
    #long_description = readme(),
    #long_description_content_type = 'text/markdown',
    license='LICENSE.txt',
    url = 'https://github.com/eabase/mt4pycon/',
    packages = find_packages(),
    scripts=['con2mtapi.py', 'liveTicks.py'],
    keywords = 'mt4 mt5 mql metaquotes metatrader api mtapi port pipe pip package',
    install_requires=[
        'pythonnet',
    ],
    python_requires = '>=3',
    classifiers=[
        # https://pypi.org/classifiers/
        #'Private :: Do Not Upload',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        #'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries',
        #'Topic :: Software Development :: Version Control',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
    ],
    project_urls={
        'Bug Reports' : 'https://github.com/eabase/mt4pycon/issues',
        'MT API Repo' : 'https://github.com/vdemydiuk/mtapi',
        #'Funding' : 'https://donate.pypi.org',
        #'Credits' : 'http://saythanks.io/to/example',
        #'Source'  : 'https://github.com/pypa/sampleproject/',
    },
    #zip_safe = False,
)
