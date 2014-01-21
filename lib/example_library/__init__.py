#!/usr/bin/env python
"""
This is a placeholder tool used only as an example.  This docstring
should consist of a high level explanation of what the functions included
are to accomplish and any other shared libraries that are necessary for
execution.
"""

#Next should be your imports which should follow the pep8 standards:
#Built in modules;
#Third party modules;
#Your own custom imports.
#i.e.

#import os # <- Built in module
#import pyyaml # <- Third party module
#import ms_net # <- Microsoft made custom import

__author__ = "Test User<test@microsoft.com>"
__copyright__ = "copyrighted by Microsoft"
__credits__ = ["Test User"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Test User"
__email__ = "test@microsoft.com"
__status__ = "Development"  # <-"Prototype", "Development", or "Production"


"""
.. module:: useful_library_1
   :platform: Unix, Windows
   :synopsis: A useful library module indeed.

.. moduleauthor:: Test User <testuser@microsoft.com>

"""


class _MySharedLibraryClass(object):
    """We use this as a shared library class example class.

    You never call this class before calling
    :func:`public_fn_with_sphinxy_docstring`.

    .. note::

       An example of intersphinx is this:
       you **cannot** use :mod:`pickle` on this class.

    """

    def __init__(self, foo, bar='baz'):
        """A really simple class.

        Args:
           foo (str): We all know what foo does.

        Kwargs:
           bar (str): Really, same as foo.

        """
        self._foo = foo
        self._bar = bar

