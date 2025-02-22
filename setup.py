# -*- coding: utf-8 -*-
import io
from setuptools import find_packages, setup

package_name = 'nexus3-cli'
package_version = '5.0.0'

requires = [
    'click>=8.0.1,<9',
    'click_aliases>=1.0.1,<2',
    'inflect>=5.3.0,<6',
    'requests[security]>=2.14.2,<3',
    'semver>=2.10.1,<3',
    'texttable>=1.6.2,<2',
    'twine>=3.4.1,<4'
]

test_requires = [
    'codecov',
    'flake8',
    'pytest',
    'pytest-cov',
    'pytest-helpers-namespace',
    'pytest-mock',
    'pytest-faker',
]

with io.open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    author='Thiago Figueiró',
    name=package_name,
    version=package_version,
    description='A python-based CLI for Sonatype Nexus OSS 3',
    url='https://gitlab.com/thiagoconde-oss/nexus3-cli',
    long_description=readme,
    long_description_content_type="text/markdown",
    setup_requires=["pytest-runner"],
    install_requires=requires,
    tests_require=test_requires,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.10,<4',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        'nexuscli': ['script/groovy'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'nexus3=nexuscli.cli:nexus_cli',
        ],
    },
    extras_require={'test': test_requires},
)
