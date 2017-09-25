#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time

class OKadminFinder():
    """
    Main class for work OKadminFinder
    """

    def __init__(self):
        # Create headers information to requests
        self.header = {}
        self.timeout = 0

    def checkUrl(self, url, proxies):
        """
        Check target url for HTTPerrors. If Error -> False, If Not Errors-> True
        :param url: string
        :return: boolean
        """

        try:

            # Timeout before check url
            time.sleep(self.timeout)

            # Get connection to target and raise exception if have errors
            req = requests.get('http://' + url, headers=self.header, proxies=proxies)
            req.raise_for_status()
            return True

        except requests.RequestException:
            return False

    @staticmethod
    def getUrls(filePath):
        """
        Create array from file with potential admin panels
        :return: array
        """

        # Open files with urls of admin panel.
        f = open(filePath, 'r')
        links = []

        # Appending to array all lines from file.
        for line in f.readlines():

            # Strip \n symbols
            links.append(line.replace('\n', ''))
        return links

    @staticmethod
    def createReqLink(site, subLink, proxies):
        """
        Create full link to potential admin panel site+sublink or subdomen+site
        :param site: string
        :param subLink: string
        :return: string
        """

        # This checking for domain or subdomain target url
        if subLink[0:3] == '%s/':
            # Create a full target url
            reqLink = subLink % site

        else:
            # Checking for www. and kill it
            if site[0:4] == 'www.':
                site = site.replace('www.', '')

                # Create a full target url for subdomains with www
                reqLink = 'www.' + subLink % site

            else:
                # Create a full target url for subdomains without www
                reqLink = subLink % site

        # Replace http:// for next use in function checkUrl
        return reqLink
