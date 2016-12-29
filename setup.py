from setuptools import setup, find_packages

setup(
	name='stopwatch',
	version='0.1.0',
	description='Simple Python module to keep track of multiple concurrent timers.',
	url='',
	author='Drew Nutter',
	author_email='',
	license='GPLv3',
	packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
	zip_safe=False
)