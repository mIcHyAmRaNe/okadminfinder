## OKadminFinder: Easy way to find admin panel of site

*OKadminFinder is an Apache2 Licensed utility, rewritten in **Python 3.x**, for admins/pentesters who want to find admin panel of a website. There are many other tools but not as effective and secure. Yeah, Okadminfinder has the the ability to use tor and hide your identity*

* ## Usage
    * #### Linux
    ```
    git clone https://github.com/Ghostboy-287/okadminfinder3.git
    cd okadminfinder3
    chmod +x okadminfinder.py
    python3 okadminfinder.py
    ```
    
    * #### Windows
    download & extract [zip](https://github.com/Ghostboy-287/okadminfinder3/archive/master.zip)  
    ```
    cd okadminfinder3
    py -3 okadminfinder.py
    ```
    
    * #### [Pentestbox](https://pentestbox.com) (same procedure as Linux)  
        you can add an alias by adding this line: `okadminfinder=py -3 "%pentestbox_ROOT%/bin/Path/to/okadminfinder3/okadminfinder.py" $*` to `C://Pentestbox/bin/customtools/customaliases` file and so you'll be able to launch it using      `okadminfinder`
    
    
* ## Requirements
    * #### Linux
    ```
    sudo apt install tor
    pip3 install --user -r requirements.txt
    ```
    
    * #### Windows
    download [tor expert bundle](https://www.torproject.org/dist/torbrowser/7.0.6/tor-win32-0.3.1.7.zip)  
    `pip3 install -r requirements.txt`
    
## Features
- [x] More than 500 potential admin panels 
- [x] Tor & Proxy
- [x] Random-agents
- [x] Console work with params, like: `okadminfinder.py -u example.com --proxy 127.0.0.1:8080`
- [ ] Classify [admin panel links](https://github.com/Ghostboy-287/okadminfinder3/blob/master/LinkFile/adminpanellinks.txt) by popularity
- [ ] Multithreading, for faster work
- [ ] Adding more potential admin panel pages
    
## Youtube videos
[okadminfinder : admin page finder](https://youtu.be/DluCL4aA9UU/)
