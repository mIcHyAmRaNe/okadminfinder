OKadminFinder: Easy way to find admin panel of site
===================================================

OKadminFinder is an Apache2 Licensed utility, rewritten in **Python 3.x**, for admins/pentesters who want to find admin panel of a website.
There are many other tools but not as effective and secure. Yeah, Okadminfinder has the the ability to use tor and hide your identity


Tested in:
----
Linux, Pentestbox, Windows

Work with Tor:
----
Windows: `Tor Bundle <https://www.torproject.org/dist/torbrowser/7.0.5/tor-win32-0.3.0.10.zip/>`_

Linux: ``apt install tor``

Requirements
----
.. code-block:: Requirements:
    
``pip3 install -r requirements.txt``
    ...

Usage
----
**in Python:**

.. code-block:: python

    >>> okadminfinder.py
    ...

**in Bash:**

.. code-block:: bash

    $ python3 okadminfinder.py
    ...

**in Pentest Box (if customaliase are):**

.. code-block:: cmd

    C:/PentestBoxDir okadminfinder
    ...

If you wanna use this tool in `Pentest Box <https://pentestbox.com/>`_, place this files to ``C://Pentestbox/bin/path/to/okadminfinder``
After that, you must add custom alias.

#. (If you don't have customaliases file) Create a file with name customaliases and place it in ``C://Pentestbox/bin/customtools/``. Please note file should not have any extension and make sure encoding is ANSI

#. Write to this file: ``okadminfinder=py -3 "%pentestbox_ROOT%/bin/Path/to/okadminfinder3/okadminfinder.py" $*``


Extensions
----------
If you know potential admin panels, you can add them to ``LinkFile/links.txt`` and/or suggest them to us `here <https://github.com/Ghostboy-287/okadminfinder3/pulls/>`_

All links use ``%s`` variable. %s = our site

Example: site = test.com -> `%s/admin` -> `test.com/admin`


In Future
---------
#.  ̶r̶a̶n̶d̶o̶m̶-̶a̶g̶e̶n̶t̶s̶ and ̶[̶p̶r̶o̶x̶y̶ ̶&̶ ̶t̶o̶r̶ ̶f̶e̶a̶t̶u̶r̶e̶s̶]̶
#.  ̶b̶e̶a̶u̶t̶i̶f̶u̶l̶ ̶a̶n̶d̶ ̶s̶i̶m̶p̶l̶e̶ ̶i̶n̶t̶e̶r̶f̶a̶c̶e̶
#. Multithreading work, for faster work.
#. Console work with params, like: okadminfinder -u --proxy --threads
#. Adding more potential admin panel pages

Youtube videos:
---------------
`okadminfinder : admin page finder <https://youtu.be/DluCL4aA9UU/>`_
