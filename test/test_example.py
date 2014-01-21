#!/usr/bin/env python
"""
Outline what the test file is expected to cover and specifically call out the shared libraries/bin,
class and functions.
"""
import os, sys
########
# Append the parent directory bin/* to path so that we can test classes and functions from within the parent directory
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir+'/lib')
sys.path.append(parentdir+'/bin')

from nose.tools import *

# Import example code from bin directory
import example_code
# Import example library from lib directory
import example_library

def test():
    """Simple test to determine if assertion engine is functioning"""
    assert True

def test_example_code_class():
    """Validate loading example_code.MyPublicClass"""
    myclass = example_code.MyPublicClass('foo', 'bar')
    assert myclass
    assert myclass._foo == 'foo'
    assert myclass._bar == 'bar'

def test_example_library_class():
    """Validate loading example_library._MySharedLibraryClass"""
    myclass = example_library._MySharedLibraryClass('foo', 'bar')
    assert myclass
    assert myclass._foo == 'foo'
    assert myclass._bar == 'bar'

def test_device_connector_class():
    """Validate that the connection class is functioning as expected."""
    devicename = "router"
    command = "dir flash:"

    """create a connection object"""
    device_connection = example_code.ExampleDeviceConnector(devicename)
    assert device_connection

    """connect using the connection object"""
    assert device_connection.get_connection()

    """execute command on connected device"""
    assert device_connection.run_command(command)
