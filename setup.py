"""Setup file for the project"""

from setuptools import find_packages, setup

setup(
    name="rest-server-example",  # what you want to call the archive/egg
    version="0.0.1",
    packages=find_packages('src'),  # top-level python modules you can import like
    package_dir={'':'src'},  # set the directory where find the package
    install_requires=['Flask==1.0.2'],
    setup_requires=["pytest-runner"],
    test_require=["pytest==4.0.1"],
    author="Vincent Vollaro",
    description="An example of program in Python",
    keywords="example tutorial",
    url="")
