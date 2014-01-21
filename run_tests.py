#!/usr/bin/env python
"""
run.py attempts to load setup.py and execute all smoke tests and readys code for code review submission
"""
########
# Append lib directory to path
import sys, os
sys.path.append('./lib')

import time
import compiler
import inspect
import subprocess
import ConfigParser
import logging
import nose
from rainbow_logging_handler import RainbowLoggingHandler
timestamp = time.strftime('%x %X %z')


########
# Read configuration file
config = ConfigParser.RawConfigParser()
config.read('{}/configuration/default.cfg'.format(os.getcwd()))


########
# Determine executing OS and build path to test directory
test_dir =  ('{}/test'.format(os.getcwd()))
logging_dir = ('{}/logging/unit_test_output_results.xml'.format(os.getcwd()))
unit_test_dir = ('{}/logging/runtests_results.log'.format(os.getcwd()))
########
# Doc source dir
doc_source_dir = ('{}/doc/source/'.format(os.getcwd()))
########


########
# Setup logging mechanism to display results of tests.
logging.basicConfig(filename=unit_test_dir, filemode='w', level='DEBUG')
formatter = logging.Formatter("[%(asctime)s] %(name)s %(funcName)s():%(lineno)d\t%(message)s")  # same as default
logger = logging.getLogger('test_logging')

# setup `RainbowLoggingHandler`
handler = RainbowLoggingHandler(sys.stderr, color_funcName=('black', 'white', True))
handler.setFormatter(formatter)
logger.addHandler(handler)
########


########
# Gather files within the bin/lib/test directories and sub-directories
def walk_directory(directory_name, filelist=[]):
    filelist = []
    for root, subFolders, files in os.walk(directory_name):
        for file in files:
            if '.pyc' not in file:
                filelist.append(os.path.join(root,file))
    return filelist

bin = walk_directory('bin')
lib = walk_directory('lib')
test = walk_directory('test')
########


########
# Perform automatic syntax validation of files within the above directories and sub-directories
def validate_syntax(directory_name):
    for file in directory_name:
        if '.py' in file and '.pyc' not in file:
            try:
                compiler.parseFile(file)
            except Exception as e:
                logger.error('An error occured while validating build syntax in file: {}, error: {}'.format(file, e))
                sys.exit(1)

logger.info("""
Validating syntax for bin/lib/test directories.
Only errors will be reported, please wait...""")

validate_syntax(bin)
validate_syntax(lib)
validate_syntax(test)
########


########
# Generate the sphinx documentation
sphinx_rst_file = []
sphinx_rst_file.append(".. {} documentation master file, created by {}".format(config.get('Section1', 'app_name'),config.get('Section1', 'author')))
sphinx_rst_file.append("   sphinx-quickstart on {}.".format(timestamp))

sphinx_rst_file.append("""\n\nWelcome to {} documentation!\n
=======================================


Contents:

.. toctree::
   :maxdepth: 2
""".format(config.get('Section1', 'app_name')))

for filen in bin:
    if '.pyc' not in filen and '.py' in filen and '__init__' not in filen:
        filename = filen.replace('.py', '').replace('\\', '.').replace('/', '.')
        imp_name = filename.replace('bin.','')
        exec "import {} as {}".format(filename, imp_name)
        sphinx_rst_file.append('.. automodule:: {}\n'.format(filename.replace('bin.', '')))

        for name, obj in inspect.getmembers(locals()[imp_name]):
            if inspect.isclass(obj):
                classname = obj.__name__
                sphinx_rst_file.append('.. autoclass:: {}\n    :members:\n'.format(classname))

sphinx_rst_file.append("""
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
""")
########


########
# Write index.rst file for sphinx autodocumentation module.
with open('{}/index.rst'.format(doc_source_dir), 'w') as file:
    for item in sphinx_rst_file:
        file.write('{}\n'.format(item))

if 'nt' in os.name:
    os.chdir('{}\\doc\\source'.format(os.getcwd()))
    sph_doc_gen = ('make.bat html')
    command = '{}'.format(sph_doc_gen)
else:
    doc_dir = '{}/doc/source/'.format(os.getcwd())
    sph_doc_gen = ('sphinx-build -b html {} {}_build/'.format(doc_dir,doc_dir))
    command = sph_doc_gen

print 'running {}'.format(command)
process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)

process.wait()
process.poll()
if process.returncode:
    raise 'Error returned during auto documentation building. Exiting.'
    sys.exit(1)
########

########
# Perform all nose unit tests
logger.info("""\n
########################\n
# Running unit tests\n
########################\n\n""")
if 'nt' in os.name:
    # Execute tests within a windows based system directly
    nose.main(argv=['-w', test_dir, '-v', '--with-doctest', '--with-xunit', '--xunit-file='+logging_dir])
else:
    # Prepare list of unit tests files and execute.
    test.remove('test/__init__.py')
    csv_test = ','.join([str(i) for i in test])
    nose.main(argv=['--tests', csv_test, '-v', '--with-doctest', '--with-xunit', '--xunit-file='+logging_dir])
