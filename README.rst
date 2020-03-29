========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        |
        | |scrutinizer|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/betwixt/badge/?style=flat
    :target: https://readthedocs.org/projects/betwixt
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/riccardomurri/betwixt.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/riccardomurri/betwixt

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/riccardomurri/betwixt?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/riccardomurri/betwixt

.. |requires| image:: https://requires.io/github/riccardomurri/betwixt/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/riccardomurri/betwixt/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/betwixt.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/betwixt

.. |commits-since| image:: https://img.shields.io/github/commits-since/riccardomurri/betwixt/v1.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/riccardomurri/betwixt/compare/v1.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/betwixt.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/betwixt

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/betwixt.svg
    :alt: Supported versions
    :target: https://pypi.org/project/betwixt

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/betwixt.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/betwixt

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/riccardomurri/betwixt/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/riccardomurri/betwixt/


.. end-badges

Easily make named infix binary operators in Python.

Demo time::

  # the only useful function in the module
  >>> from betwixt import infix_operator

  # any function of 2 arguments would do
  >>> from fnmatch import fnmatch

  # make the binary function into an operator, delimited by `*`
  >>> matches = infix_operator('*', fnmatch)

  # use it
  >>> 'foo.txt' *matches* '*.txt'
  True

  # other delimiters can be used
  >>> matches = infix_operator('|', fnmatch)
  >>> 'foo.txt' |matches| '*.txt'
  True

A decorator form can also be used::

  >>> @infix_operator('|')
  ... def contains(left, right):
  ...   return right in left

  >>> [1, 2, 3] |contains| 1
  True

  >>> [1, 2, 3] |contains| 0
  False

Finally, ``betwixt`` is provided as a shorter (and, perhaps, more
expressive) alias to ``infix_operator``::

  >>> from betwixt import betwixt

  >>> @betwixt('*')
  ... def joining(left, right):
  ...   return left.join(right)

  >>> '_' *joining* ['a', 'b', 'c']
  'a_b_c'

  >>> split_at = betwixt('//', lambda lhs, rhs: lhs.split(rhs))

  >>> 'a_b_c' //split_at// '_'
  ['a', 'b', 'c']

All these example operators and a few more are available in module
``betwixt.examples``.

The idea was taken from
http://code.activestate.com/recipes/384122-infix-operators/ and by a
similar C++ hack whose code on the web I cannot find any more, but no
actual code has been stolen.


Installation
============

::

    pip install betwixt

Documentation
=============


https://betwixt.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox


Copyright and license
=====================

Copyright (c) 2016-2020 Riccardo Murri <riccardo.murri@gmail.com>

This is free software, available under the terms and conditions
of the GNU LGPL -- see file LICENSE for details.
