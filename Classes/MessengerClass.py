#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Messenger():
    """
    Class for printing colored messages
    """

    def __init__(self):
        from colorama import Fore
        # Creating styling for simple use
        self.style = {'white': Fore.WHITE, 'red': Fore.RED, 'green': Fore.GREEN, 'yellow': Fore.YELLOW, 'blue': Fore.BLUE, 'cyan': Fore.CYAN}


    def writeMessage(self, message, color='white'):
        """
        Write message to console with color. Colors - white, red, green, yellow
        :param message: string
        :param color: string
        :return:
        """

        print (self.style[color] + message)


    def writeInput(self, message, color='white'):
        """
        Create input with color text. Colors - white, red, green, yellow
        :param message: string
        :param color: string
        :return: input
        """
        try:
            return input(self.style[color] + message)
        except:
            self.writeMessage('Invalid value. Try again', 'red')
            return self.writeInput(self.style[color] + message)

    def writeInput(self, message, color='white'):
        """
        Create input with color text. Colors - white, red, green, yellow
        :param message: string
        :param color: string
        :return: input
        """
        try:
            return input(self.style[color] + message)
        except:
            self.writeMessage('Invalid value. Try again', 'red')
            return self.writeInput(self.style[color] + message)

    def writeInputWithYesNo(self, message, color='white'):
        """
        Create input yes/no with Yes default and color text. Colors - white, red, green, yellow
        :param message: string
        :param color: string
        :return: input
        """
        valueOfInput = self.writeInput('%s [Y][n]  $ ' % message, color)
        if valueOfInput == '' or valueOfInput == 'y' or valueOfInput == 'Y':
            return True
        elif valueOfInput == 'n' or valueOfInput == 'N':
            return False
        else:
            self.writeMessage('Invalid value %s. Try again' % valueOfInput, 'red')
            return self.writeInputWithYesNo(message, color)
