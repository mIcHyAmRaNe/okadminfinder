#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    # Change main dir to this (need for Pentest Box)
    import os
    os.path.abspath(__file__)
    from Classes import (Credits,
                         OKadminFinderClass,
                         MessengerClass)

    import urllib.request, urllib.error, urllib.parse
    import requests
    import socket
    import socks
    import sys
    from urllib.request import urlopen
    from colorama import Fore, Back, Style

    # Get Messenger class to print information
    messenger = MessengerClass.Messenger()

except():
    exit('\n\t[x] Session Cancelled; Something wrong with import modules')

try:
    # Get credits and print it
    messenger.writeMessage(Credits.getCredits()[0], 'green')

    # Get main class object
    OKadminFinder = OKadminFinderClass.OKadminFinder()

    # Add header from credits
    OKadminFinder.header = {'user-agent': 'OKadminFinder/%s' % Credits.getCredits()[1]}

    # Additional params
    # if not messenger.writeInputWithYesNo(Fore.YELLOW + '  Do you want use default params?'):
    #     timeout = messenger.writeInput(Fore.YELLOW + '  Change timeout. Please write value in seconds: ' + Fore.GREEN)
    #     OKadminFinder.timeout = timeout

    #network params
    choice=''
    print(Fore.YELLOW+'    ┌───['+Fore.CYAN+'Network settings:'+Fore.YELLOW+']');
    while (choice not in ['1','2','3','tor','proxy']):
        choice=input(Fore.YELLOW+'''    ┊
    ├╼[1] tor
    ├╼[2] proxy
    ├╼[3] nothing
    ┊
    └───╼['''+Fore.RED+'''Please choose one option'''+Fore.YELLOW+'''] ~$ ''')
        if choice=='1' or choice=='tor':
            socks.set_default_proxy(socks.SOCKS5, 'localhost', 9050)
            socket.socket = socks.socksocket
            urllib.request.urlopen
            proxies=""

        elif choice=='2' or choice=='proxy':
            prox=input('''    ┊
    └────► set your HTTP proxy {example:127.0.0.1:80} : ~$ ''')
            proxies = {
              'http': 'http://'+prox,
              'https': 'http://'+prox,
            }

        else:
            proxies=""
            continue

    messenger.writeMessage('''    ┆
    ├─[Your IP address]
    ┆''','cyan');
    print('    └─────►',requests.get('http://ip.42.pl/raw',proxies=proxies).text)
    print('')
    # Get site
    site = messenger.writeInput('  Enter Site Name  { example : example.com or www.example.com } \n' +Fore.BLUE +' ~$ ', 'white'); print ('')

    if OKadminFinder.checkUrl(site,proxies):
        messenger.writeMessage('\n  Site %s is stable\n' % site,'green')
    else:
        messenger.writeMessage('  Something wrong with url', 'red')
        exit(SystemExit)

    # Get links for checking
    urls = OKadminFinder.getUrls('LinkFile/adminpanellinks.txt')

    # Counters for total links, and admin panel find
    totalCount = len(urls)
    adminCount = 0

    # Checking all links
    for url in urls:

        # Create test link with getting params from input and links.txt file
        reqLink = OKadminFinder.createReqLink(site, url, proxies)
        messenger.writeMessage('\t [#] Checking http://' + reqLink, 'yellow')

        # Test created link for HTTPerrors. If not error - potential admin panel
        if OKadminFinder.checkUrl(reqLink,proxies):
            adminCount += 1
            messenger.writeMessage('  %s %s' % ('\n  [✔] http://' + reqLink, 'Admin page found!'), 'bright')

            # Stopped process? and waiting for input for continue
            messenger.writeInput('  Press enter to continue scanning.\n')

        # If HTTPerrors continue testing other links
        else:
            continue

    # Write last information about scanning with counters
    messenger.writeMessage('\n\n  Completed \n', 'green')
    messenger.writeMessage(str(adminCount) + ' Admin pages found', 'white')
    messenger.writeMessage(str(totalCount) + ' total pages scanned', 'white')
    messenger.writeInput('  [/] Scanning over; Press Enter to Exit', 'green')

    # This magic for Pentest Box. This is return normal color style of console
    messenger.writeMessage('','white')

except (KeyboardInterrupt, SystemExit):
    messenger.writeMessage('\n\t[!] Session Cancelled', 'red')

    # This magic for Pentest Box. This is return normal color style of console
    messenger.writeMessage('','white')

except():
    messenger.writeMessage('\n\t[!] Session Cancelled; Unknown error', 'red')

    # This magic for Pentest Box. This is return normal color style of console
    messenger.writeMessage('','white')
