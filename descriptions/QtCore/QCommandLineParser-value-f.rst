.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (const QString&) const
    :digest: 4d207d64649a80e3ddf43597ca5d9683

Returns the option value found for the given option name *optionName*, or an empty string if not found.

The name provided can be any long or short name of any option that was added with :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addOption`. All the option names are treated as being equivalent. If the name is not recognized or that option was not present, an empty string is returned.

For options found by the parser, the last value found for that option is returned. If the option wasn't specified on the command line, the default value is returned.

If the option does not take a value, a warning is printed, and an empty string is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser.values`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValue`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValues`.
