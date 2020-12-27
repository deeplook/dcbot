# -*- coding: utf-8 -*-

import re
import os
from setuptools import setup, find_packages


if __name__ == "__main__":
    module_name = 'simplebot_here'

    init_file = os.path.join(module_name, '__init__.py')
    with open(init_file) as fh:
        version = re.search(
            r'version = \'(.*?)\'', fh.read(), re.M).group(1)

    with open('README.rst') as fh:
        long_description = fh.read()
    with open('CHANGELOG.rst') as fh:
        long_description += fh.read()
    with open('LICENSE') as fh:
        long_description += fh.read()

    setup(
        name=module_name,
        version=version,
        description='A plugin for SimpleBot, a Delta Chat(http://delta.chat/) bot',
        long_description=long_description,
        long_description_content_type='text/x-rst',
        keywords='simplebot plugin deltachat here',
        license='MPL',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Plugins',
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
            'Operating System :: OS Independent',
            'Topic :: Utilities',
        ],
        zip_safe=False,
        include_package_data=True,
        packages=find_packages(),
        install_requires=[
            'simplebot',
            'requests',
        ],
        entry_points={
            'simplebot.plugins': '{0} = {0}'.format(module_name),
        },
    )
