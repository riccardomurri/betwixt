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
.. |docs| image:: https://readthedocs.org/projects/inbetween/badge/?style=flat
    :target: https://readthedocs.org/projects/inbetween
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/riccardomurri/inbetween.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/riccardomurri/inbetween

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/riccardomurri/inbetween?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/riccardomurri/inbetween

.. |requires| image:: https://requires.io/github/riccardomurri/inbetween/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/riccardomurri/inbetween/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/inbetween.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/inbetween

.. |commits-since| image:: https://img.shields.io/github/commits-since/riccardomurri/inbetween/v1.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/riccardomurri/inbetween/compare/v1.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/inbetween.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/inbetween

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/inbetween.svg
    :alt: Supported versions
    :target: https://pypi.org/project/inbetween

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/inbetween.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/inbetween

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/riccardomurri/inbetween/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/riccardomurri/inbetween/


.. end-badges

Easily make named infix binary operators in Python.

Demo time::

  # the only useful function in the module
  >>> from inbetween import make_infix_operator

  # any function of 2 arguments would do
  >>> from fnmatch import fnmatch

  # make the binary function into an operator, delimited by `*`
  >>> matches = make_infix_operator(fnmatch, '*')

  # use it
  >>> 'foo.txt' *matches* '*.txt'
  True

  # other delimiters can be used
  >>> matches = make_infix_operator(fnmatch, '|')
  >>> 'foo.txt' |matches| '*.txt'
  True

The idea was taken from
http://code.activestate.com/recipes/384122-infix-operators/ and by a
similar C++ hack whose code on the web I cannot find any more, but no
actual code has been stolen.


Installation
============

::

    pip install inbetween

Documentation
=============


https://inbetween.readthedocs.io/


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
