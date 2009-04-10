# setup.py
from distutils.core import setup
from glob import glob

#windows installer:
# python setup.py bdist_wininst

setup(
    name="pyserial",
    description="Python Serial Port Extension",
    version="1.16",
    author="Chris Liechti",
    author_email="cliechti@gmx.net",
    url="http://pyserial.sourceforge.net/",
    packages=['serial'],
    license="Python",
    long_description="Python Serial Port Extension for Win32, Linux, BSD, Jython"
)