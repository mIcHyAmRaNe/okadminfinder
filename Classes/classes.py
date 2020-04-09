#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import contextlib
from colorama import Fore, Style
import httpx
import random
import trio
from tqdm.auto import tqdm
import time
import sys

blue = Fore.BLUE
red = Fore.RED
cyan = Fore.CYAN
green = Fore.GREEN
magenta = Fore.MAGENTA
RESET = Fore.RESET
DIM = Style.DIM
NORMAL = Style.NORMAL
BOLD = Style.BRIGHT
RESET_ALL = Style.RESET_ALL

@contextlib.contextmanager
def credit():
    t0 = time.time()
    print(green,BOLD,'''
     _______ _     _           _       _         ___ _           _
    ( ______( )   | |         | |     (_)       / __(_)         | |
    | |     | |___| |_____  __| |____  _ ____ _| |__ _ ____   __| |_____  ____
    | |   | |  _   _(____ |/ _  |    \| |  _ (_   __| |  _ \ / _  | ___ |/ ___)
    | |___| | |  \ \/ ___ ( (_| | | | | | | | || |  | | | | ( (_| | ____| |
     \_____/|_|   \_\_____|\____|_|_|_|_|_| |_||_|  |_|_| |_|\____|_____|_|
          version 2.6 created by O.Koleda & rewrited by mIcHy AmRaNe

        ''',RESET_ALL)


    yield
    print(green,'''\tThank you for using OKadminFinder''',RESET_ALL)
    print(green, DIM,'\tTime needed : %.2fs'
              % (time.time() - t0), RESET_ALL)

def get_agents():
    agents_path = 'LinkFile/user-agent.txt'
    with open(agents_path, 'r') as ua:
        for line in ua:
            rua = random.choice(list(ua))
            agent = {'user-agent': rua.rstrip()}
        return agent

def get_links():
    links_path = 'LinkFile/adminpanellinks.txt'
    links = []
    with open(links_path, 'r') as apl:
        for line in apl:
            links.append(line.replace('\n', ''))
    return links

def create_link(website):
    try:
        url = httpx.URL(website)
        reqlinks = []
    except httpx.InvalidURL:
        sys.exit('''
        Invalid URL: example.com
        Valid URL: http://example.com, http://www.example.com
        ''')
    if url.host[0:4] == 'www.':
        website = url.host.replace('www.', '')
        for n in get_links():
            req_link = url.scheme + '://' + n.format(website)
            reqlinks.append(req_link.replace('\n', ''))
    else:
        website = url.host
        for n in get_links():
            req_link = url.scheme + '://' + n.format(website)
            reqlinks.append(req_link.replace('\n', ''))
    return reqlinks

def check_url(website, headers, proxies):
    with httpx.Client(headers=headers, proxies=proxies) as client:
        try:
            req = client.get(website)
            req.raise_for_status
            return True
        except (httpx.HTTPError, httpx.NetworkError):
            return False
def proxy(prox, headers):
    try:
        proxies = {
             "http": f"http://{prox}",
             "https": f"http://{prox}"
            }
        with httpx.Client(headers=headers, proxies=proxies) as client:
            test = client.get('https://httpbin.org/get')
    except (httpx.NetworkError, httpx.ProxyError):
        print('\n\t┎───[', red, BOLD, 'Proxy/Network Error', RESET_ALL, ']')
        print('\t┠───╸', magenta, 'Check the proxy format | Reminder: 127.0.0.1:8080', RESET_ALL)
        print('\t┠───╸', magenta, 'Check the proxy quality', RESET_ALL)
        print('\t┖───╸', magenta, 'Check your connection', RESET_ALL)
        sys.exit(1)
    return proxies

async def url(website, headers, proxies):
    try:
        if check_url(website, headers, proxies):
            print(magenta, DIM, website,RESET_ALL,green, 'is stable\n', RESET_ALL)
        else:
            print(red, DIM,'Seems something wrong with url', RESET_ALL)
            sys.exit(1)
        urls = create_link(website)
        admin_count = 0
        total_count = len(urls)
        pbar = tqdm(total=total_count, bar_format=('{l_bar}'+DIM+'{bar}'+RESET_ALL+'|{n_fmt}/{total_fmt}{postfix}'))
        async with httpx.AsyncClient(headers=headers, proxies=proxies) as client:
            for url in urls:
                pbar.update()
                try:
                    response = await client.get(url)
                    if response.status_code == httpx.codes.OK:
                        tqdm.write(f"{green} ҂ Found: {cyan} {url} {RESET_ALL} \n")
                        admin_count += 1
                    else:
                        continue
                except (httpx.NetworkError, httpx.ReadTimeout, httpx.ConnectTimeout, httpx.ProxyError):
                    continue
            pbar.close()
        print('\n\n\t╔═══[✔️]',green,BOLD,' Completed',RESET_ALL)
        print('\t╟───╸📑️', str(admin_count), 'Admin pages found')
        print('\t╚═══[📚️]', str(total_count), 'total pages scanned')
    except(KeyboardInterrupt, SystemExit):
        pbar.close()
        print(red,'\n\tSession Canceled', RESET_ALL)
