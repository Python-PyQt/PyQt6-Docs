.. sip:method-description::
    :status: todo
    :pysig: 3c9a938a1e983dbe538fd869f2db5e67
    :realsig: () const
    :digest: 0421befa0bd4c072a3eeac2ebcb989a2

Returns a list of option names that were found.

This returns a list of all the recognized option names found by the parser, in the order in which they were found. For any long options that were in the form {–option=value}, the value part will have been dropped.

The names in this list do not include the preceding dash characters. Names may appear more than once in this list if they were encountered more than once by the parser.

Any entry in the list can be used with :sip:ref:`~PyQt6.QtCore.QCommandLineParser.value` or with :sip:ref:`~PyQt6.QtCore.QCommandLineParser.values` to get any relevant option values.
