from setuptools import find_packages, setup

import okadminfinder as meta

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="okadminfinder",
    version=meta.__version__,
    author=meta.__maintainer__,
    author_email="michyamrane@gmail.com",
    description="[ Admin panel finder / Admin Login Page Finder ] ¢σ∂є∂ ву 👻 (❤-❤) 👻",  # noqa: E501
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mIcHyAmRaNe/okadminfinder3",
    packages=find_packages(),
    package_data={"": ["okadminfinder/LinkFile/*.txt"], },
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["okadminfinder = okadminfinder.okadminfinder:main", ]  # noqa: E501
    },
)
