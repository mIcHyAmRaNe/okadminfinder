![](https://gist.githubusercontent.com/mIcHyAmRaNe/0b370c808bd1a600778f6a3875e5a732/raw/35f2803c176eeb27d4eea5eac88087b0d78f0ecc/okadminfinder3-.png)

[![GitHub license](https://img.shields.io/github/license/mIcHyAmRaNe/okadminfinder3.svg)](https://github.com/mIcHyAmRaNe/okadminfinder/blob/master/LICENSE)
![](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20osx-lightgrey.svg)
[![GitHub stars](https://img.shields.io/github/stars/mIcHyAmRaNe/okadminfinder3.svg?style=social)](https://github.com/mIcHyAmRaNe/okadminfinder/stargazers)
[![Downloads](https://static.pepy.tech/badge/okadminfinder/week)](https://pepy.tech/project/okadminfinder)
[![Downloads](https://static.pepy.tech/badge/okadminfinder)](https://pepy.tech/project/okadminfinder)

## OKadminFinder: Easy way to find [Admin panel - Directories - Subdomains] of website

*OKadminFinder is an Apache2 Licensed utility, rewritten in **Python 3.x**, for admins/pentesters who want to find [Admin panel - Directories - Subdomains] of a website. There are many other tools but not as effective and secure. Yeah, Okadminfinder has the the ability to use tor and hide your identity*

* ## Requirements
    ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
    ![PyPI](https://img.shields.io/pypi/v/argparse.svg?label=argparse)
    ![PyPI](https://img.shields.io/pypi/v/colorama.svg?label=colorama)
    ![PyPI](https://img.shields.io/pypi/v/httpx.svg?label=httpx)
    ![PyPI](https://img.shields.io/pypi/v/trio.svg?label=trio)
    ![PyPI](https://img.shields.io/pypi/v/tqdm.svg?label=tqdm)
    * #### Linux
       ```bash
       ❯ sudo apt install tor
       ❯ sudo service tor start
       ```

    * #### Windows
       download [tor windows expert bundle](https://www.torproject.org/download/tor/)

* ## Preview
   <a href="http://www.youtube.com/watch?feature=player_embedded&v=5C9aOinwKAs" target="_blank">
      <img src="https://i.imgur.com/610tOPC.png" alt="Watch the video" border="10" />
   </a>

* ## Installation
      
   * #### PyPi
      ```bash
      # Install
      ❯ pip install okadminfinder
      # Update
      ❯ pip install --upgrade okadminfinder
      # Remove
      ❯ pip uninstall okadminfinder


      # Usage
      ❯ okadminfinder -h
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

## Features
- [x] Multiplatforms `(Windows/Linux/MacOS)`
- [x] Easy to install, update and even remove
- [x] More than 1000 potential admin panels
- [x] Ability to find subdomains (equivalent to fuzz.URL)
- [x] Custom wordlist (e.g: /usr/share/wordlist/sub-domains.txt)
- [x] Console works with params, like: `❯ okadminfinder -u https://example.com --proxy 127.0.0.1:8080`
- [x] Random-Agents
- [x] HTTP/HTTPS Proxies
- [x] Socks4/5 & Tor
- [x] Debug mode

## Developer section

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

  * #### Debian
      ```bash
      # Install Poetry
      curl -sSL https://install.python-poetry.org | python3 -
      # Install buid requirements 
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
      # before building a new version, make sure to 
   ```

## Youtube videos
- [okadminfinder : PyPi version](https://youtu.be/5C9aOinwKAs/)
- [okadminfinder : admin page finder](https://youtu.be/DluCL4aA9UU/)
- [okadminfinder3 : admin page finder (update)](https://youtu.be/iJg4NJT5qkY/)
- [admin panel finder Kali Linux 2018.3](https://youtu.be/kY9KeDqY5QQ)

## Most Blogs that shared okadminfinder
- [kitploit.com](https://www.kitploit.com/2019/04/okadminfinder3-admin-panel-finder-admin.html)
- [securityonline.info](https://securityonline.info/admin-login-page-finder/)
- [prodefence.org](https://www.prodefence.org/okadminfinder3-admin-login-page-finder/)
- [kalilinuxtutorials.com](https://kalilinuxtutorials.com/okadminfinder-admin-panel/)
- [onehack.us](https://onehack.us/t/how-to-find-website-admin-panel-using-okadminfinder-tool-easy-method/64840)
- [the-realworld.org](https://the-realworld.org/okadminfinder-finder-du-panneau-dadministration-finder-admin-page-finder)
- [crackitdown.com](https://www.crackitdown.com/2019/12/find-admin-panel-using-OkadminFinder.html)
- [securitynewspaper.com](https://www.securitynewspaper.com/2020/01/02/find-hidden-admin-page-of-any-website/)
