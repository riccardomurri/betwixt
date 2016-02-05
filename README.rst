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
