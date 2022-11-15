from setuptools import setup

import openets

setup(
    name='openets',
    version=openets.__version__,
    packages=['openets'],
    url='https://github.com/nikprodev/openets',
    license='MIT',
    author='Nikita Strelkov',
    author_email='nikprodev@gmail.com',
    description='Open event ticketing system',
    install_requires=['django==4.1.3', 'pytz'],
    zip_safe=True,
    include_package_data=True,
)
