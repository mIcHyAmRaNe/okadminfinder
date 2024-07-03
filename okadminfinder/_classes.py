#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os.path import dirname, isfile
from sys import exit
import contextlib
import random
import time

import httpx
import socksio
from colorama import Fore, Style
from tqdm.auto import tqdm

import okadminfinder as meta

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


class okadminfinder:
    @contextlib.contextmanager
    def credit(self):
        t0 = time.time()
        print(
            green,
            BOLD,
            f"""
         _______ _     _           _       _         ___ _           _
        ( ______( )   | |         | |     (_)       / __(_)         | |
        | |     | |___| |_____  __| |____  _ ____ _| |__ _ ____   __| |_____  ____
        | |   | |  _   _(____ |/ _  |    \| |  _ (_   __| |  _ \ / _  | ___ |/ ___)
        | |___| | |  \ \/ ___ ( (_| | | | | | | | || |  | | | | ( (_| | ____| |
         \_____/|_|   \_\_____|\____|_|_|_|_|_| |_||_|  |_|_| |_|\____|_____|_|
            💚 version {meta.__version__} created by {meta.__creator__} & recoded by {meta.__maintainer__} 💚

            """,  # noqa: W605 E501
            RESET_ALL,
        )

        yield
        print(green, """\tThank you for using OKadminFinder""", RESET_ALL)
        print(
            green, DIM, f"\tTime needed : {(time.time() - t0):.2f}", RESET_ALL
        )  # noqa: E501

    def get_agents(self):
        agents_path = str(dirname(meta.__file__) + "/LinkFile/user-agent.txt")
        with open(agents_path, "r") as ua:
            for line in ua:
                rua = random.choice(list(ua))
                agent = {"user-agent": rua.rstrip()}
            return agent

    def get_links(dns=False, wordlist=None):
        links = []
        
        if dns and not wordlist:
            links_path = str(dirname(meta.__file__) + "/LinkFile/subdomains-top1million-5000.txt")
        elif wordlist:
            if not isfile(wordlist):
                print(red, "\n\tError: The wordlist file does not exist.", RESET_ALL)
                exit(1)
            links_path = str(wordlist)
        else:
            links_path = str(dirname(meta.__file__) + "/LinkFile/adminpanellinks.txt")

        with open(links_path, "r") as apl:
            for line in apl:
                line = line.strip()
                if dns:
                    line = f"{line}.{{}}"
                    links.append(line.replace("\n", ""))
                if line.startswith("{}") or line.endswith("{}"):
                    links.append(line.replace("\n", ""))
                elif line.startswith("#"):
                    pass
                else:
                    line = f"{{}}/{line}"
                    links.append(line.replace("\n", ""))
        return links

    def create_link(website, dns=False, wordlist=None):
        try:
            url = httpx.URL(website)
            reqlinks = []
        except httpx.InvalidURL:
            exit(
                """
            Invalid URL: example.com
            Valid URL: http://example.com, http://www.example.com
            """
            )
        if url.host[0:4] == "www.":
            website = url.host.replace("www.", "")
            for n in okadminfinder.get_links(dns, wordlist):
                req_link = url.scheme + "://" + n.format(website)
                reqlinks.append(req_link.replace("\n", ""))
        else:
            website = url.host
            for n in okadminfinder.get_links(dns, wordlist):
                req_link = url.scheme + "://" + n.format(website)
                reqlinks.append(req_link.replace("\n", ""))
        return reqlinks

    def check_url(website, headers, proxies):
        with httpx.Client(headers=headers, proxies=proxies) as client:
            try:
                req = client.get(website)
                req.raise_for_status
                return True
            except (httpx.HTTPError, httpx.NetworkError):
                return False

    def get_proxy(prox):
        return prox

    def proxy(self, prox, headers):
        try:
            proxies = okadminfinder.get_proxy(prox)
            with httpx.Client(headers=headers, proxies=proxies) as client:
                client.get("https://httpbin.org/get")
        except (
            httpx.NetworkError,
            httpx.ProxyError,
            httpx.ReadTimeout,
            httpx.ConnectTimeout,
            socksio.exceptions.ProtocolError,
        ):
            print(
                "\n\t┎───[", red, BOLD, "Proxy/Network Error", RESET_ALL, "]"
            )  # noqa: E501
            print(
                "\t┠───╸",
                magenta,
                BOLD,
                "Check the proxy format | Reminder::: http(s) format:: 127.0.0.1:8080  ,  socks format:: socks5://127.0.0.1:1080",
                RESET_ALL,
            )
            print(
                "\t┠───╸", magenta, BOLD, "Check the proxy quality", RESET_ALL
            )  # noqa: E501
            print("\t┖───╸", magenta, BOLD, "Check your connection", RESET_ALL)
            exit(1)

        except (KeyboardInterrupt):
            print(red, "\n\tSession Canceled", RESET_ALL)
            exit(0)
        return proxies

    async def url(self, website, headers, proxies, dns=False, wordlist=None):
        try:
            if okadminfinder.check_url(website, headers, proxies):
                print(
                    magenta,
                    BOLD,
                    website,
                    RESET_ALL,
                    green,
                    "is stable\n",
                    RESET_ALL,  # noqa: E501
                )
            else:
                print(red, DIM, "Seems something wrong with url", RESET_ALL)
                exit(1)
            urls = okadminfinder.create_link(website, dns, wordlist)
            admin_count = 0
            total_count = len(urls)
            pbar = tqdm(
                total=total_count,
                leave=False,
                bar_format=(
                    "{l_bar}"
                    + DIM
                    + "{bar}"
                    + RESET_ALL
                    + "|{n_fmt}/{total_fmt}{postfix}"
                ),
            )
            async with httpx.AsyncClient(
                headers=headers, proxies=proxies
            ) as client:  # noqa: E501
                for url in urls:
                    pbar.update()
                    try:
                        response = await client.get(url)
                        if (
                            response.status_code == httpx.codes.OK
                            or response.status_code == httpx.codes.MOVED_PERMANENTLY
                        ):
                            tqdm.write(
                                f"{green} ҂ Found: {cyan} {url} {RESET_ALL} \n"
                            )  # noqa: E501
                            admin_count += 1
                        else:
                            continue
                    except (
                        httpx.NetworkError,
                        httpx.ReadTimeout,
                        httpx.ConnectTimeout,
                        httpx.ProxyError,
                    ):
                        continue
                pbar.close()
            print("\n\n\t╔═══[✓]", green, BOLD, "Completed", RESET_ALL)
            print("\t╟───[⚛]", str(admin_count), "Pages found")
            print("\t╚═══[∞︎︎]", str(total_count), "Total pages scanned")
        except (KeyboardInterrupt):
            pbar.close()
            print(red, "\n\tSession Canceled", RESET_ALL)
            exit(0)
        except (SystemExit):
            print(red, "\n\tSession Canceled", RESET_ALL)
            exit(1)
