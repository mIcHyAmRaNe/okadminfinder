![](https://gist.githubusercontent.com/mIcHyAmRaNe/0b370c808bd1a600778f6a3875e5a732/raw/35f2803c176eeb27d4eea5eac88087b0d78f0ecc/okadminfinder3-.png)
![GitHub License](https://img.shields.io/github/license/michyamrane/okadminfinder?style=for-the-badge&logo=github&color=dodgerblue)
![Static Badge](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20osx-lightgrey?style=for-the-badge&color=slategray)
![GitHub Repo stars](https://img.shields.io/github/stars/michyamrane/okadminfinder?style=for-the-badge&logo=github&logoColor=black&labelColor=snow&color=slategray)
![PyPI - Downloads](https://img.shields.io/pypi/dw/okadminfinder?style=for-the-badge&color=dodgerblue)
![Pepy Total Downloads](https://img.shields.io/pepy/dt/okadminfinder?style=for-the-badge&logo=pypi&logoColor=snow&color=dodgerblue)

## Overview

OKadminFinder is a powerful, open-source tool designed to help administrators and penetration testers discover admin panels, directories, and subdomains of a website.\
Built with Python 3.x, OKadminFinder offers a robust set of features to ensure effective and secure scanning.

## Features

  - [x] Multi-Platform Support: Works on Windows, Linux, and macOS.
  - [x] Easy Installation and Updates: Simple commands to install, update, and remove the tool.
  - [x] Extensive Admin Panel Database: Over 1600 potential admin panels.
  - [x] Command-Line Interface: Works with parameters for flexible usage.
  - [x] Target URL: Specify the target URL for scanning.
  - [x] URLs File: Specify a file containing a list of URLs to scan.
  - [x] Random User Agents: Helps avoid detection by using random user agents.
  - [x] Proxy Support: Supports HTTP/HTTPS proxies.
  - [x] Socks4/5 & Tor: Enhanced anonymity with Socks4/5 and Tor support.
  - [x] Custom Wordlists: Use your own wordlists for more targeted scanning.
  - [x] DNS Mode: Use DNS mode for wordlist scanning.
  - [x] Subdomain Discovery: Equivalent to fuzz.URL for finding subdomains.
  - [x] Fuzzing Mode: Use fuzzing mode for more dynamic URL testing.
  - [x] File Extensions: Search for specific file extensions.
  - [x] Status Codes: Specify valid HTTP status codes or ranges.
  - [x] Custom Cookies: Set custom cookies for requests.
  - [x] Support for Authentication: Use custom username and password for secure access during scans.
  - [x] Output File: Save results to an output file.
  - [x] Cache Management: Clear and disable the cache for fresh scans.
  - [x] Timeout Settings: Customize timeout settings for requests.
  - [x] Connection Pools: Adjust the number of connection pools for better performance.
  - [x] Threading: Control the number of threads for concurrent processing.
  - [x] Retry Mechanism: Set the number of retries for failed requests.
  - [x] Delay Customization: Fine-tune delay between requests to control response times.
  - [x] Debug Mode: Detailed logging for debugging purposes.

* ## Requirements

![Python](https://img.shields.io/badge/Python-3-dodgerblue?style=for-the-badge&logo=python&logoColor=yellow)
![Dependencies](https://img.shields.io/badge/Dependencies-typer%20%7C%20rich%20%7C%20urllib3-dodgerblue?style=for-the-badge&logo=python&logoColor=white)
![Dev Dependencies](https://img.shields.io/badge/Dev%20Dependencies-pytest%20%7C%20ruff-forestgreen?style=for-the-badge&logo=pytest&logoColor=white)

  * #### Linux

      ```bash
      ❯ sudo apt install tor
      ❯ sudo service tor start
      ```

  * #### Windows

    Download [tor windows expert bundle](https://www.torproject.org/download/tor/)

* ## Installation

  * #### PyPi

    ```bash
    # Install
    ❯ pip install okadminfinder
    # Update
    ❯ pip install --upgrade okadminfinder
    # Remove
    ❯ pip uninstall okadminfinder
    ```

  * #### Git Clone
    
    ```bash
    # Download and Usage
    ❯ git clone https://github.com/mIcHyAmRaNe/okadminfinder.git
    ❯ cd okadminfinder
    ❯ pip3 install -r requirements.txt
    ❯ chmod +x okadminfinder.py
    ❯ ./okadminfinder.py -h
    ```

## Preview

<div style="width: 100%; max-width: 600px; margin: 0 0 0 55px; background: var(--color-canvas-default, #ffffff); border: 1px solid var(--color-border-default, #ddd); border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); overflow: hidden;">
  <a href="https://youtu.be/vU5R9OoMqFc?si=Rees4MV9FfL9xgf9" target="_blank">
    <img src="https://i.imgur.com/KdlHadA.png" alt="Watch the video" style="width: 100%; display: block;" />
  </a>
</div>


## Usage

  * ### Basic Usage

    ```bash
    # Scanning a Single URL
    ❯ okadminfinder --url https://example.com
        
    # Scanning Multiple URLs from a File
    ❯ okadminfinder --urls-file urls.txt
        
    # Using a Custom Wordlist
    ❯ okadminfinder --url https://example.com --wordlist custom_wordlist.txt
        
    # Using Random User Agents
    ❯ okadminfinder --url https://example.com --random-agent
        
    # Using a Proxy
    ❯ okadminfinder --url https://example.com --proxy 127.0.0.1:8080
        
    # Using Tor for Anonymity
    ❯ okadminfinder --url https://example.com --tor
    ```

    > [!IMPORTANT]
    > Parameter Conflicts:\
    > Proxy and Tor: You cannot use both a proxy and Tor at the same time.\
    > DNS Mode and Fuzzing Mode: You cannot use both DNS mode and fuzzing mode at the same time.\
    > Files Option and Non-Fuzzing Mode: The --files option can only be used with the fuzzing mode.\
    > URL and URLs File: You cannot provide both a single URL and a file containing multiple URLs at the same time.

  * ### Advanced Usage

    For more advanced usage examples and detailed documentation, an Advanced Wiki is under construction.

## Developer Section

  * #### PyPi

    ```bash
    # Install Poetry
    curl -sSL https://install.python-poetry.org | python3 -
    
    # Clone the repo
    git clone https://github.com/mIcHyAmRaNe/okadminfinder.git
    
    # Build the project
    poetry build
    
    # Publish the package
    poetry publish
    ```
    
* #### Debian (planned)

    ```bash
    # Install Poetry
    curl -sSL https://install.python-poetry.org | python3 -
    
    # Install build requirements
    sudo apt install debhelper dh-python python3-setuptools python3-all pybuild-plugin-pyproject
    
    # Clone the repo
    git clone https://github.com/mIcHyAmRaNe/okadminfinder.git
    
    # Create the source tarball
    tar czf okadminfinder_{version}.orig.tar.gz okadminfinder
    
    # Get inside the project folder
    cd okadminfinder
    
    # Build the deb package
    dpkg-buildpackage -rfakeroot -uc -us

    # Notes:
    # Steps from Python to Debian.
    # Install Stdeb
    pip install stdeb
    # Debianize Python package creating debian folder
    python3 setup.py --command-packages=stdeb.command debianize
    # we edit rules, control files, we create changelog, man pages...
    # Build deb package
    dpkg-buildpackage -rfakeroot -uc -us
    # before building a new version, make sure to clean it first
    ```
## YouTube Videos

  - [OKadminFinder 2.0: Take Control of Your Admin Panel Discovery!](https://youtu.be/vU5R9OoMqFc?si=oXCJv77PbZwL4IEI)

## Disclaimer

> [!IMPORTANT]
> OKadminFinder is intended for educational purposes and authorized penetration testing only.
> Usage of OKadminFinder for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Donate

> [!INFO]
> If you find OKadminFinder useful and would like to support its development, you can donate to the following address:\
> **Bitcoin Address:** `1LZiNVRZupWNbB9bEPxsiwoC5AGPAuFCjp` \
> Your support is greatly appreciated ♥️

