.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: 7e88feb063241debc8cb620bdd9a6b70

Returns a list of option names that were found.

This returns a list of all the recognized option names found by the parser, in the order in which they were found. For any long options that were in the form {--option=value}, the value part will have been dropped.

The names in this list do not include the preceding dash characters. Names may appear more than once in this list if they were encountered more than once by the parser.

Any entry in the list can be used with ``value()`` or with ``values()`` to get any relevant option values.
