"""
Examples of `betwixt` operators usage.
"""
# Examples in this file are organized by theme and/or the Python
# module they wrap; disable a few std pylint warnings that conflict
# with this structure.
#
# pylint: disable=invalid-name
# pylint: disable=wrong-import-order
# pylint: disable=wrong-import-position

from . import betwixt, infix_operator


@infix_operator('|')
def contains(left, right):
    """
    Return ``True`` if sequence *right* occurs in sequence *left*.
    Delimited by ``|``.

    This is an alias for Python expression ``right in left``.

    Examples::

      >>> [1, 2, 3] |contains| 1
      True

      >>> [1, 2, 3] |contains| 0
      False

      >>> "foobar" |contains| "a"
      True
    """
    return right in left


@infix_operator('*')
def joining(left, right):
    """
    Concatenate strings in sequence *right*, separating them with *left*.
    Delimited by ``*``.

    This is an alias for ``str.join(left, right)``.

    Example::

      >>> '_' *joining* ['a', 'b', 'c']
      'a_b_c'
    """
    return left.join(right)


@infix_operator('//')
def split_at(left, right):
    """
    Split string *left* at every occurrence of string *right*.
    Delimited by ``//``.

    This is just an alias for Python's ``left.split(right)``.

    Example::

      >>> 'a_b_c' //split_at// '_'
      ['a', 'b', 'c']
    """
    return left.split(right)


@infix_operator('<<')
def then(lhs, rhs):
    """
    Apply right-hand side to left-hand side.
    Delimited by ``<<`` and ``>>``.

    In other words, this is a way of writing function composition in
    application order::

      # these two are exactly equivalent
      y = f(g(h(x)))
      y = h(x) <<then>> g <<then>> f

    This can be useful to rewrite "pipelines" with a more readable
    syntax.  For example, this code::

      raw_config = _read_config_files(paths)
      tree_config1 = _arrange_config_tree(raw_config)
      tree_config2 = _perform_key_renames(tree_config1)
      complete_config = _build_node_section(tree_config2)
      object_tree = _validate_and_convert(complete_config)
      deref_config = _dereference_config_tree(object_tree)
      final_config = _cross_validate_final_config(deref_config)

    can be rewritten in this way::

      final_config = (
        _read_config_files(paths)
        <<then>> _arrange_config_tree
        <<then>> _perform_key_renames
        <<then>> _build_node_section
        <<then>> _validate_and_convert
        <<then>> _dereference_config_tree)
    """
    return rhs(lhs)


import fnmatch

matches = infix_operator('/', fnmatch.fnmatchcase)
"""
Check if left-hand side matches the glob expression on the right-hand side.
Delimited by ``/``.

Examples::

  >>> 'foo.txt' /matches/ '*.txt'
  True

  >>> 'bar.jpg' /matches/ '*.png'
  False
"""

matching = infix_operator('/', fnmatch.filter)
"""
Given a list on the left-hand side, return list of
items that match the glob pattern on the right-hand side.
Delimited by ``/``.

Examples::

  >>> ['foo.txt', 'bar.txt', 'quux.png'] /matching/ '*.txt'
  ['foo.txt', 'bar.txt']

  >>> ['foo.txt', 'bar.txt', 'quux.png'] /matching/ '*.pjg'
  []
"""


import os

join = infix_operator('/', os.path.join)
"""
Append relative path the the right-hand side to the patch on the left.
Delimited by ``/``.

This is just Python's standard `os.path.join` recast in infix form.

Examples::

  >>> '/tmp' /join/ 'foo'
  '/tmp/foo'

  >>> '.' /join/ 'bar'
  './bar'
"""
