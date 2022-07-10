from setuptools import find_packages, setup
setup(
    name='chain_agnostic_lib',
    packages=find_packages(include=['chain_agnostic_lib']),
    version='0.1.0',
    description='Chain Agnostic Library',
    author='Kirill Balakhonov - github.com/balakhonoff',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner', 'web3'],
    tests_require=['pytest==7.1.2'],
    test_suite='tests',
)