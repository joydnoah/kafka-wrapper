from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='kafka',
    url='https://github.com/tykiblood/kafka-wrapper',
    author='Sebastian Quinones',
    author_email='ingesql1992@hotmail.com',
    # Needed to actually package something
    packages=['kafka-utils-wrapper'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)