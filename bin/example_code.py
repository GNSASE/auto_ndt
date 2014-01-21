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
import re
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
.. module:: useful_1
   :platform: Unix, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: Test User <testuser@microsoft.com>


"""

class PromptMatchError(Exception):
    """Custom exception for ExampleDeviceConnector class"""
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)


class ConnectionError(Exception):
    """Custom exception for ExampleDeviceConnector class"""
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)


class CommandExecutionError(Exception):
    """Custom exception for ExampleDeviceConnector class"""
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)


def public_fn_with_googley_docstring(name, state=None):
    """This function does something.

    Args:
       name (str):  The name to use.

    Kwargs:
       state (bool): Current state to be in.

    Returns:
       int.  The return code::

          0 -- Success!
          1 -- No good.
          2 -- Try again.

    Raises:
       AttributeError, KeyError

    A really great idea.  A way you might use me is

    >>> print public_fn_with_googley_docstring(name='foo', state=None)
    0

    BTW, this always returns 0.  **NEVER** use with :class:`MyPublicClass`.

    """
    return 0


def public_fn_with_sphinxy_docstring(name, state=None):
    """This function does something.

    :param name: The name to use.
    :type name: str.
    :param state: Current state to be in.
    :type state: bool.
    :returns:  int -- the return code.
    :raises: AttributeError, KeyError

    """
    return 0


def public_fn_without_docstring():
    return True


def _private_fn_with_docstring(foo, bar='baz', foobarbas=None):
    """I have a docstring, but won't be imported if you just use ``:members:``.
    """
    return None


class _MyNotSoPublicClass(object):
    """We use this as a not so public class example class.

    You never call this class before calling :func:`public_fn_with_sphinxy_docstring`.

    .. note::

       An example of intersphinx is this: you **cannot** use :mod:`pickle` on this class.

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


class MyPublicClass(object):
    """We use this as a public class example class.

    You never call this class before calling :func:`public_fn_with_sphinxy_docstring`.

    .. note::

       An example of intersphinx is this: you **cannot** use :mod:`pickle` on this class.

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

    def get_foobar(self, foo, bar=True):
        """This gets the foobar

        This really should have a full function definition, but I am too lazy.

        >>> print get_foobar(10, 20)
        30
        >>> print get_foobar('a', 'b')
        ab

        Isn't that what you want?

        """
        return foo + bar

    def _get_baz(self, baz=None):
        """A private function to get baz.

        This really should have a full function definition, but I am too lazy.

        """
        return baz


class ExampleDeviceConnector(object):
    """

    This is an example script that will create an object containing
    mocking as though its connecting to a router and returning output.

    """

    def __init__(self, devicename):
        """This class will attempt to make a connection
        to a device and execute a command based upon the
        input provided by the user at time of execution.

        Args:
           devicename (str): The device hostname that you wish to connect.

        Kwargs:
           command (str): Command that you wish to execute.

        """
        self._devicename = devicename


    def get_connection(self):
        """This function sets up the connection object.

        IF this was an actual working example the ssh / telnet connection
        would be established here.  For the sake of example the string is
        what you could possibly expect when making the connection.
        """
        self._connection_output = """
                                  Attempting to make a connection to {}.
                                  Connection to {} has been made successfully.
                                  router>
                                  """.format(self._devicename, self._devicename)

        if not self._connection_output:
            raise ConnectionError("Connection attempt to {} has failed. Exiting".format(self._devicename))

        cisco_prompt_regex = re.compile(r"{}(>|#)".format(self._devicename))

        if not cisco_prompt_regex.search(self._connection_output):
            raise PromptMatchError("Invalid prompt detected for {}. Exiting".format(self._devicename))

        return self._connection_output

    def run_command(self, command=""):
        """This function will attempt to execute the provided command
        from the user on the device using the connection object made
        previously.

        Kwargs:
           command (str): Command that you wish to execute.

        """

        if not command:
            raise CommandExecutionError("You did not specify a command. Exiting.")

        self._command = command

        self._command_output = """
        Router> dir flash:

Directory of flash:/


program load complete, entry point: 0x8000f000, size: 0xc0c0


Initializing ATA monitor library.......
Directory of flash:


2      29823132  -rw- c2800-adventerprisek9-mz
                              """

        cisco_error_regex = re.compile(r"ERROR: %".format(self._devicename))

        if not self._command_output:
            raise CommandExecutionError("Command did not execute successfully. Exiting.")
        if cisco_error_regex.search(self._command_output):
            raise CommandExecutionError("Command reported an error. Exiting.")


        return self._command_output
