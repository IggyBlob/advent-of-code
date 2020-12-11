from setuptools import setup, find_packages

setup(
    name="advent-of-code",
    version="0.1",
    description="IggyBlob's solutions for https://adventofcode.com/",
    url="https://github.com/IggyBlob/advent-of-code",
    author="IggyBlob",
    author_email="myusername@example.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.8.0",
        "numpy",
        "parse",
        "networkx"
        # list your other requirements here, for example:
        # "numpy", "parse", "networkx",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["IggyBlob = solutions:solve"],
    },
)
