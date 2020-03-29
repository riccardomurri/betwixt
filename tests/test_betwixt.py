#
# Test suite for the `betwixt` package
#

from fnmatch import fnmatch

from betwixt import *


class TestDelimitedInfixOperator(object):
    """
    Test operator creation via `*DelimitedInfixOperator` classes.
    """

    def test_double_star_delimited_operator(self):
        matches = DoubleStarDelimitedInfixOperator(fnmatch)
        assert ('foo.txt' **matches** '*.txt')

    def test_star_delimited_operator(self):
        matches = StarDelimitedInfixOperator(fnmatch)
        assert ('foo.txt' *matches* '*.txt')

    def test_plus_delimited_operator(self):
        matches = PlusDelimitedInfixOperator(fnmatch)
        assert ('foo.txt' +matches+ '*.txt')

    def test_bar_delimited_operator(self):
        matches = BarDelimitedInfixOperator(fnmatch)
        assert ('foo.txt' |matches| '*.txt')

    def test_caret_delimited_operator(self):
        matches = CaretDelimitedInfixOperator(fnmatch)
        assert ('foo.txt' ^matches^ '*.txt')

    def test_slash_delimited_operator(self):
        matches = SlashDelimitedInfixOperator(fnmatch)
        assert ('foo.txt' /matches/ '*.txt')

    def test_double_slash_delimited_operator(self):
        matches = DoubleSlashDelimitedInfixOperator(fnmatch)
        assert ('foo.txt' //matches// '*.txt')

    def test_angle_delimited_operator(self):
        matches = AngleDelimitedInfixOperator(fnmatch)
        assert ('foo.txt' <<matches>> '*.txt')


class Test_infix_operator(object):
    """
    Test operator creation via `infix_operator`.
    """

    def test_star_delimited_operator(self):
        matches = infix_operator('*', fnmatch)
        assert ('foo.txt' *matches* '*.txt')

    def test_double_star_delimited_operator(self):
        matches = infix_operator('**', fnmatch)
        assert ('foo.txt' **matches** '*.txt')

    def test_slash_delimited_operator(self):
        matches = infix_operator('/', fnmatch)
        assert ('foo.txt' /matches/ '*.txt')

    def test_double_slash_delimited_operator(self):
        matches = infix_operator('//', fnmatch)
        assert ('foo.txt' //matches// '*.txt')

    def test_angle_delimited_operator(self):
        matches = infix_operator('<<', fnmatch)
        assert ('foo.txt' <<matches>> '*.txt')

    def test_plus_delimited_operator(self):
        matches = infix_operator('+', fnmatch)
        assert ('foo.txt' +matches+ '*.txt')

    def test_caret_delimited_operator(self):
        matches = infix_operator('^', fnmatch)
        assert ('foo.txt' ^matches^ '*.txt')

    def test_bar_delimited_operator(self):
        matches = infix_operator('|', fnmatch)
        assert ('foo.txt' |matches| '*.txt')


class Test_infix_operator_as_decorator(object):
    """
    Test that `infix_operator` works as function decorator.
    """

    def test_star_delimited_operator(self):
        @infix_operator('*')
        def matches(lhs, rhs):
            return fnmatch(lhs, rhs)
        assert ('foo.txt' *matches* '*.txt')

    def test_double_star_delimited_operator(self):
        @infix_operator('**')
        def matches(lhs, rhs):
            return fnmatch(lhs, rhs)
        assert ('foo.txt' **matches** '*.txt')

    def test_slash_delimited_operator(self):
        @infix_operator('/')
        def matches(lhs, rhs):
            return fnmatch(lhs, rhs)
        assert ('foo.txt' /matches/ '*.txt')

    def test_double_slash_delimited_operator(self):
        @infix_operator('//')
        def matches(lhs, rhs):
            return fnmatch(lhs, rhs)
        assert ('foo.txt' //matches// '*.txt')

    def test_angle_delimited_operator(self):
        @infix_operator('<<')
        def matches(lhs, rhs):
            return fnmatch(lhs, rhs)
        assert ('foo.txt' <<matches>> '*.txt')

    def test_plus_delimited_operator(self):
        @infix_operator('+')
        def matches(lhs, rhs):
            return fnmatch(lhs, rhs)
        assert ('foo.txt' +matches+ '*.txt')

    def test_caret_delimited_operator(self):
        @infix_operator('^')
        def matches(lhs, rhs):
            return fnmatch(lhs, rhs)
        assert ('foo.txt' ^matches^ '*.txt')

    def test_bar_delimited_operator(self):
        @infix_operator('|')
        def matches(lhs, rhs):
            return fnmatch(lhs, rhs)
        assert ('foo.txt' |matches| '*.txt')
