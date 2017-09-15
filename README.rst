OKadminFinder: Easy way to find admin panel of site
===================================================

OKadminFinder is an Apache2 Licensed utility, rewritten in Python 3.x, for admins/pentesters who want to find admin panel of a website.
There are many other tools but not as effective and secure. Yeah, Okadminfinder has the the ability to use tor and hide your identity

OKadminFinder created for `Pentest Box <https://pentestbox.com/>`_, but you can use it on windows; Linux & Mac


Tested in:
----
Pentestbox, Windows & Linux

Work with Tor:
----
Windows: `Tor Bundle <https://www.torproject.org/dist/torbrowser/7.0.5/tor-win32-0.3.0.10.zip/>`_

Linux: ``apt install tor``

Requirements
----
.. code-block:: Requirements:
    
``pip install -r requirements.txt``
    ...

Used
----
**in Python:**

.. code-block:: python

    >>> okadminfinder.py
    ...

**in Bash:**

.. code-block:: bash

    $ python okadminfinder.py
    ...

**in Pentest Box (if customaliase are):**

.. code-block:: cmd

    C:/PentestBoxDir okadminfinder
    ...

If you wanna use this tool in `Pentest Box <https://pentestbox.com/>`_, place this files to ``C://Pentestbox/bin/path/to/okadminfinder``
After that, you must add custom alias.

#. (If you don't have customaliases file) Create a file with name customaliases and place it in ``C://Pentestbox/bin/customtools/``. Please note file should not have any extension and make sure encoding is ANSI

#. Write to this file: ``okadminfinder=python "%pentestbox_ROOT%/bin/Path/to/okadminfinder3/okadminfinder.py" $*``


Extensions
----------
If you know potential admin panels, you can add them to ``LinkFile/links.txt`` and/or suggest them to us `here <https://github.com/Ghostboy-287/okadminfinder3/pulls/>`_

All links use ``%s`` variable. %s = our site

Example: site = test.com -> `%s/admin` -> `test.com/admin`


In Future
---------
#. Config file with network params, like proxy, headers etc.
#. Multithreading work, for faster work. Adding more potential admin panel pages
#. Console work with params, like: okadminfinder -u --proxy --threads
