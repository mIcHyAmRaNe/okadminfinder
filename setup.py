from setuptools import setup, find_packages
import os

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

def get_files(directory, filetypes):
    return [os.path.join(directory, f) for f in os.listdir(directory) if any(f.endswith(ft) for ft in filetypes)]

setup(
    name="okadminfinder",
    version="1.1.0",
    description="[Admin panel - Directories - Subdomains] finder ¢σ∂є∂ ву 👻 (❤-❤) 👻",
    author="mIcHyAmRaNe",
    author_email="6m63er17c@mozmail.com",
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://michyamrane.github.io/tools/okadminfinder/",
    project_urls={
        "Bug Tracker": "https://github.com/mIcHyAmRaNe/okadminfinder/issues",
        "Repository": "https://github.com/mIcHyAmRaNe/okadminfinder",
    },
    keywords=[
        "security-scanner",
        "pentest-tool",
        "admin-page-finder",
        "okadminfinder"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Natural Language :: English"
    ],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    data_files=[
        ('/usr/share/okadminfinder', ['LICENSE', 'README.md']),
        ('/usr/share/okadminfinder/LinkFile', get_files('okadminfinder/LinkFile', ['txt'])),
    ],
    python_requires=">=3.7",
    install_requires=[
        "argparse>=1.4.0",
        "colorama>=0.4.6",
        "httpx[socks]>=0.23.1",
        "trio>=0.22.0",
        "tqdm>=4.64.1"
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=22.12.0"
        ]
    },
    entry_points={
        "console_scripts": [
            "okadminfinder=okadminfinder.okadminfinder:main"
        ]
    }
)
