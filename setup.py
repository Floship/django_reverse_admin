from distutils.core import setup

setup(
    name='Django Reverse Admin',
    version='0.0.1',
    packages=['django_reverse_admin'],
    install_requires=['django-nested-admin'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)
