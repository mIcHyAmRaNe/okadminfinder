![](./Classes/okadminfinder3-.svg)
<p align="center">
  <a href="https://www.buymeacoffee.com/michyamrane" target="_blank">
    <img width="170" height="37" alt="Buy Me A Coffee" src="https://camo.githubusercontent.com/031fc5a134cdca5ae3460822aba371e63f794233/68747470733a2f2f7777772e6275796d6561636f666665652e636f6d2f6173736574732f696d672f637573746f6d5f696d616765732f6f72616e67655f696d672e706e67">
  </a>
</p>

[![Build Status](https://travis-ci.org/mIcHyAmRaNe/okadminfinder3.svg?branch=master)](https://travis-ci.org/mIcHyAmRaNe/okadminfinder3)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
[![GitHub license](https://img.shields.io/github/license/mIcHyAmRaNe/okadminfinder3.svg)](https://github.com/mIcHyAmRaNe/okadminfinder3/blob/master/LICENSE)
![](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20osx-lightgrey.svg)
[![GitHub stars](https://img.shields.io/github/stars/mIcHyAmRaNe/okadminfinder3.svg?style=social)](https://github.com/mIcHyAmRaNe/okadminfinder3/stargazers)

## OKadminFinder: Easy way to find admin panel of site

*OKadminFinder is an Apache2 Licensed utility, rewritten in **Python 3.x**, for admins/pentesters who want to find admin panel of a website. There are many other tools but not as effective and secure. Yeah, Okadminfinder has the the ability to use tor and hide your identity*

* ## Requirements
    ![PyPI](https://img.shields.io/pypi/v/argparse.svg?label=argparse)
    ![PyPI](https://img.shields.io/pypi/v/colorama.svg?label=colorama)
    ![PyPI](https://img.shields.io/pypi/v/PySocks.svg?label=PySocks)
    ![PyPI](https://img.shields.io/pypi/v/tqdm.svg?label=tqdm)
    ![PyPI](https://img.shields.io/pypi/v/requests.svg?label=requests)
    * #### Linux
       ```
       sudo apt install tor
       sudo apt install python3-socks  (optional)
       pip3 install --user -r requirements.txt
       ```

    * #### Windows
       download [tor expert bundle](https://dist.torproject.org/torbrowser/8.0.8/tor-win32-0.3.5.8.zip)
       `pip3 install -r requirements.txt`

* ## Usage
    * #### Preview
       [![asciicast](https://asciinema.org/a/209959.png)](https://asciinema.org/a/209959)

    * #### Linux
       ```
       git clone https://github.com/mIcHyAmRaNe/okadminfinder3.git
       cd okadminfinder3
       chmod +x okadminfinder.py
       python3 okadminfinder.py
       ```

    * #### Windows
       download & extract [zip](https://github.com/mIcHyAmRaNe/okadminfinder3/archive/master.zip)
       ```
       cd okadminfinder3
       py -3 okadminfinder.py
       ```

    * #### [Pentestbox](https://pentestbox.com) (same procedure as Linux)
        you can add an alias by adding this line: `okadminfinder=py -3 "%pentestbox_ROOT%/bin/Path/to/okadminfinder3/okadminfinder.py" $*` to `C://Pentestbox/bin/customtools/customaliases` file and so you'll be able to launch it using      `okadminfinder`


## Features
- [x] More than 500 potential admin panels
- [x] Tor & Proxy
- [x] Random-Proxy
- [x] Random-Agents
- [x] Console work with params, like: `okadminfinder.py -u example.com --proxy 127.0.0.1:8080`
- [x] Self-Update
- [ ] Classify [admin panel links](https://github.com/mIcHyAmRaNe/okadminfinder3/blob/master/LinkFile/adminpanellinks.txt) by popularity
- [ ] Multithreading, for faster work
- [ ] Adding more potential admin panel pages

## Youtube videos
- [okadminfinder : admin page finder](https://youtu.be/DluCL4aA9UU/)
- [okadminfinder3 : admin page finder (update)](https://youtu.be/iJg4NJT5qkY/)
- [admin panel finder Kali Linux 2018.3](https://youtu.be/kY9KeDqY5QQ)

## Most Blogs that shared okadminfinder
- [kitploit.com](https://www.kitploit.com/2019/04/okadminfinder3-admin-panel-finder-admin.html)
- [securityonline.info](https://securityonline.info/admin-login-page-finder/)
- [prodefence.org](https://www.prodefence.org/okadminfinder3-admin-login-page-finder/)
- [kalilinuxtutorials.com](https://kalilinuxtutorials.com/okadminfinder-admin-panel/)
