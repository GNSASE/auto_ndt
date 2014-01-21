This is an example base python package for GNS development use. The purpose of this package is to provide a working foundation of a python application containing a stand-alone executable
within bin/example_code.py, a shared library module within lib/example_library/__init__.py and an example py-nose unit test in test/test_example.py.

This package is also equipped with a automatted run_tests.py file which on execution will perform syntax verification on all files within bin/ | lib/ | test/ directories, execute all
unit tests and finally attempt auto document code located within the bin/ directory.  The auto documentation will be locally accessible and found within the doc/source/_build/html/index.
Currently auto documentation is only enabled for the bin/ directory however in future releases will include the lib/ and test/ directories as well.

You should always run run_tests before submitting code for review and ensure that the logs within the logging directory are included with the review.  This will allow for the reviewer to
see the results of your tests before reviewing the code further.

*****IMPORTANT*****
Now you should also edit the configuration\default.cfg file replacing the defaults with your own information and save.
