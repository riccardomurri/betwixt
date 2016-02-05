#! /usr/bin/env python
#
# Copyright (C) 2016 Riccardo Murri <riccardo.murri@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# make coding more python3-ish, must be the first statement
from __future__ import (absolute_import, print_function)


## module doc and other metadata
"""
Infix binary operators.

Inspired by http://code.activestate.com/recipes/384122-infix-operators/
"""
__docformat__ = 'reStructuredText'
__author__ = ('Riccardo Murri <riccardo.murri@gmail.com>')


## declare public API

__all__ = [
    'make_infix_operator',
    # just in case some masochist wants to access these directly ...
    'DoubleStarDelimitedInfixOperator',
    'StarDelimitedInfixOperator',
    'SlashDelimitedInfixOperator',
    'PlusDelimitedInfixOperator',
    'AngleDelimitedInfixOperator',
    'CaretDelimitedInfixOperator',
    'BarDelimitedInfixOperator',
]


## "maker" code

class _BaseInfixOperator(object):
    __slots__ = ['_op']

    def __init__(self, func):
        self._op = func


class _BasePartialOperation(object):
    def __init__(self, op, lhs):
        self._op = op
        self._lhs = lhs


def _make_partial_operation_class(method):
    def make(cls):
        name = cls.__name__
        bases = (_BasePartialOperation,)
        body = dict(cls.__dict__)

        def stage1(self, rhs):
            return self._op(self._lhs, rhs)
        body[method] = stage1

        return type(name, bases, body)
    return make


def _make_infix_operator_class(lmeth, rmeth):
    def make(cls):
        name = cls.__name__
        bases = (_BaseInfixOperator,)
        body = dict(cls.__dict__)

        @_make_partial_operation_class(rmeth)
        class _PartialOperation:
            pass
        body['_PartialOperation'] = _PartialOperation

        def stage2(self, other):
            return self._PartialOperation(self._op, other)
        body[lmeth] = stage2

        return type(name, bases, body)
    return make


## infix operator classes, highest priority first

@_make_infix_operator_class('__rpow__', '__pow__')
class DoubleStarDelimitedInfixOperator:
    pass


@_make_infix_operator_class('__rmul__', '__mul__')
class StarDelimitedInfixOperator:
    pass

@_make_infix_operator_class('__rdiv__', '__div__')
class SlashDelimitedInfixOperator:
    pass


@_make_infix_operator_class('__rlshift__', '__rshift__')
class AngleDelimitedInfixOperator:
    pass


@_make_infix_operator_class('__radd__', '__add__')
class PlusDelimitedInfixOperator:
    pass


@_make_infix_operator_class('__rxor__', '__xor__')
class CaretDelimitedInfixOperator:
    pass


@_make_infix_operator_class('__ror__', '__or__')
class BarDelimitedInfixOperator:
    pass


_delimiter_to_class = {
    '**': DoubleStarDelimitedInfixOperator,
    '*':  StarDelimitedInfixOperator,
    '/':  SlashDelimitedInfixOperator,
    '+':  PlusDelimitedInfixOperator,
    '<<': AngleDelimitedInfixOperator,
    '^':  CaretDelimitedInfixOperator,
    '|':  BarDelimitedInfixOperator,
}

def make_infix_operator(func, delimiter):
    assert delimiter in _delimiter_to_class
    return _delimiter_to_class[delimiter](func)


## run tests

if '__main__' == __name__:

    from fnmatch import fnmatch

    #matches = DoubleStarDelimitedInfixOperator(fnmatch)
    #assert ('foo.txt' **matches** '*.txt')

    matches = StarDelimitedInfixOperator(fnmatch)
    assert ('foo.txt' *matches* '*.txt')

    matches = PlusDelimitedInfixOperator(fnmatch)
    assert ('foo.txt' +matches+ '*.txt')

    matches = BarDelimitedInfixOperator(fnmatch)
    assert ('foo.txt' |matches| '*.txt')

    matches = CaretDelimitedInfixOperator(fnmatch)
    assert ('foo.txt' ^matches^ '*.txt')

    matches = SlashDelimitedInfixOperator(fnmatch)
    assert ('foo.txt' /matches/ '*.txt')

    matches = AngleDelimitedInfixOperator(fnmatch)
    assert ('foo.txt' <<matches>> '*.txt')

    ##

    #matches = make_infix_operator(fnmatch, '**')
    #assert ('foo.txt' **matches** '*.txt')

    matches = make_infix_operator(fnmatch, '*')
    assert ('foo.txt' *matches* '*.txt')

    matches = make_infix_operator(fnmatch, '/')
    assert ('foo.txt' /matches/ '*.txt')

    matches = make_infix_operator(fnmatch, '<<')
    assert ('foo.txt' <<matches>> '*.txt')

    matches = make_infix_operator(fnmatch, '+')
    assert ('foo.txt' +matches+ '*.txt')

    matches = make_infix_operator(fnmatch, '^')
    assert ('foo.txt' ^matches^ '*.txt')

    matches = make_infix_operator(fnmatch, '|')
    assert ('foo.txt' |matches| '*.txt')

    ##

    print ("Ok.")
