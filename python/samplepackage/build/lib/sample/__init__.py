#encoding:utf-8

from __future__ import absolute_import
from __future__ import print_function
import sys,os

__version__ = "sample 1.2"


## reload the module
import imp
imp.reload(test2)

## different importing methods
from . import test2
from .test3 import *
## cannot relative import beyond top-level package
# from ..sample.test import *

__doc__ = """


## >> os.system("sudo python3 setup.py install")
## >>> os.system("sudo python3 setup.py bdist_wheel")


### different import ways
## >>> import sample
## >>> print(sample.__version__)
## sample 1.2
## >>> print(sample.__path__)
## ['/home/auss/Projects/MyGithub/ImagePy/test/sample']
## >>> print(sample.__file_)
## ['/home/auss/Projects/MyGithub/ImagePy/test/sample/__init__.py']
## >>> print(sample.__spec__)
## ModuleSpec(name='sample', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7fb156803e10>, origin='/home/auss/Projects/MyGithub/ImagePy/test/sample/__init__.py', submodule_search_locations=['/home/auss/Projects/MyGithub/ImagePy/test/sample'])
## >>> dir(sample)
## ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'absolute_import', 'imp', 'info3', 'main', 'os', 'print_function', 'show3', 'sys', 'test1', 'test2', 'test3']
###################################################################################
## 因为没有在__init__.py中导入test1 ，所以使用的时候需要导入 from sample import test1。
## 因为已经在__init__.py中导入了test2，所以可以使用          sample.test2.info3。
## 因为已经在__init__.py中导入了test3的所有模块，所以可以使用 sample.info3。
## >>> from sample import test1
## >>> print(test1.info1)
## 'This is a file in the sample/test1.py'
## >>> sample.test2.info2
## 'This is a file in the sample/test2.py'
## >>> sample.info3
## 'This is a file in the sample/test3.py'
"""

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    here =  __file__[:__file__.rfind(os.path.sep)]
    print("starting path:",here)

    print("This is the main routine.")
    print("It should do something interesting.")

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    main()
