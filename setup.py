from setuptools import setup, find_packages

import os
import sys

parent_directory = os.path.abspath(os.path.dirname(__file__))

metafiles = {
    'README.md',
    'CHANGES.md',
    'CLASSIFIERS.txt',
}

# The following bit will read each index from metafiles and fill it's value
# with the contents of that file if it is able to read the file.
for filename in metafiles:
    try:
        current_file = open(os.path.join(parent_directory, filename))
        metafiles[filename] = current_file.read()
        current_file.close()

    except IOError:
        pass

# No dependancies :)
dependancies = []

metadata = {
    'name': 'stateful-objects',
    'version': '0.0.5',
    'description': 'Implements an interface for stateful object behaviors.',
    'long_description': metafiles['README.md'] + '\n\n' + metafiles['CHANGES.md'],
    'classifiers': metafiles['CLASSIFIERS.txt'],
    'author': 'Brandon R. Stoner',
    'author_email': 'monokrome@limpidtech.com',
    'url': 'http://limpidtech.com/',
    'keywords': '',
    'packages': find_packages(),
    'include_package_data': True,
    'zip_safe': True,
    'install_requires': dependancies,
    'tests_require': dependancies,
    'test_suite': 'states',
}

setup(**metadata)
