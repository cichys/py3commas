from setuptools import find_packages, setup

setup(
    name='py3commas',
    version='0.0.6',

    description='3commas Python wrapper',

    url='https://github.com/cichys/py3commas',

    author='Stefano Cicatiello',
    author_email='ste@anche.no',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    keywords='api 3commas trading crypto bitcoin altcoin',

    packages=find_packages(exclude=['tests']),

    install_requires=[
        'requests',
    ],
)