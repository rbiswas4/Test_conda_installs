from distutils.core import setup
import sys
import os
import re

# read version number from version file.
# read version file without setting up package
packageDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          'test_imports')
versionFile = os.path.join(packageDir, 'version.py')

with open(versionFile, 'r') as f:
    s = f.read()
# Look up the string value assigned to __version__ in version.py using regexp
versionRegExp = re.compile("__version__ = \"(.*?)\"")
# Assign to __version__
__version__ =  versionRegExp.findall(s)[0]

setup(name='test_imports',
      version=__version__,
      description='testing absolute imports',
      packages=['test_imports'],
      package_dir={'test_imports': 'test_imports'},
     )
