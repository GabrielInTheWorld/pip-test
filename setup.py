import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piptest",
    version="1.0.0",
    author="GabrielInTheWorld",
    author_email="meyergabriel@live.de",
    description="Package to provide auth functionalities",
    long_description=long_description,
    url="https://github.com/GabrielInTheWorld/pip-test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
