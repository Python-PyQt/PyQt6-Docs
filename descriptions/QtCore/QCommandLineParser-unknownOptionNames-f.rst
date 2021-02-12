.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: 942c2b2e8abf69c3ad08ccf9b8615d6e

Returns a list of unknown option names.

This list will include both long an short name options that were not recognized. For any long options that were in the form {--option=value}, the value part will have been dropped and only the long name is added.

The names in this list do not include the preceding dash characters. Names may appear more than once in this list if they were encountered more than once by the parser.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser.optionNames`.
