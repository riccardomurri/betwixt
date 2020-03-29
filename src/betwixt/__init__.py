#! /usr/bin/env python
#
"""
Infix binary operators.

Inspired by http://code.activestate.com/recipes/384122-infix-operators/
"""
# Copyright (C) 2016-2020 Riccardo Murri <riccardo.murri@gmail.com>
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
from __future__ import (absolute_import, division, print_function)


## module metadata
__version__ = '1.0.0'


## declare public API

__all__ = [
    'betwixt',
    'infix_operator',
    # just in case some masochist wants to access these directly ...
    'DoubleStarDelimitedInfixOperator',
    'StarDelimitedInfixOperator',
    'SlashDelimitedInfixOperator',
    'DoubleSlashDelimitedInfixOperator',
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

# Need different code here because the order of operands in ``pow()``
# is reversed compared to the other operations.  It's just simpler to
# explicitly write the code here, than extend the "maker" methods to
# support this special case.
class DoubleStarDelimitedInfixOperator(_BaseInfixOperator):
    class _PartialOperation(_BasePartialOperation):
        def __rpow__(self, rhs):
            return self._op(rhs, self._lhs)
    def __pow__(self, other):
        return self._PartialOperation(self._op, other)


@_make_infix_operator_class('__rmul__', '__mul__')
class StarDelimitedInfixOperator:
    pass

# Likewise, different code is needed here to support *both* old-style
# division and "true" division (``from __future__ import division``).
# It's just simpler to explicitly write the code here, than extend the
# "maker" methods to support this special case.
class SlashDelimitedInfixOperator(_BaseInfixOperator):
    class _PartialOperation(_BasePartialOperation):
        def __div__(self, rhs):
            return self._op(self._lhs, rhs)
        def __truediv__(self, rhs):
            return self._op(self._lhs, rhs)
    def __rdiv__(self, other):
        return self._PartialOperation(self._op, other)
    def __rtruediv__(self, other):
        return self._PartialOperation(self._op, other)

@_make_infix_operator_class('__rfloordiv__', '__floordiv__')
class DoubleSlashDelimitedInfixOperator:
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
    '//': DoubleSlashDelimitedInfixOperator,
    '+':  PlusDelimitedInfixOperator,
    '<<': AngleDelimitedInfixOperator,
    '^':  CaretDelimitedInfixOperator,
    '|':  BarDelimitedInfixOperator,
}

def infix_operator(delimiter, *func):
    """
    """
    assert delimiter in _delimiter_to_class
    assert len(func) in [0, 1]
    # pylint: disable=no-else-return
    if func:
        # make operator
        return _delimiter_to_class[delimiter](func[0])
    else:
        # decorate a function
        return _delimiter_to_class[delimiter]

betwixt = infix_operator
"""
Alias for `infix_operator` (which see).
"""
