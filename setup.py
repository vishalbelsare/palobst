from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(packages=find_packages(),
    name="palobst",
    version="0.0.1",
    description="PaloBoost is an over-fitting robust Gradient Boosting algorithm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yubin Park",
    author_email="yubin.park@gmail.com",
    url="https://github.com/yubin-park/palobst",
    license="Apaceh 2.0", 
    install_requires = ["numpy", "numba"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ])


