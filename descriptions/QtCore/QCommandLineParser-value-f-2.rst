.. sip:method-description::
    :status: todo
    :pysig: 4fa0960f626986883b81c619e8915efb
    :realsig: (const QString&) const
    :digest: 0eaa7699d6d827bf2e1466f92f94f70f

Returns the option value found for the given option name *optionName*, or an empty string if not found.

The name provided can be any long or short name of any option that was added with :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addOption`. All the option names are treated as being equivalent. If the name is not recognized or that option was not present, an empty string is returned.

For options found by the parser, the last value found for that option is returned. If the option wasn't specified on the command line, the default value is returned.

An empty string is returned if the option does not take a value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser.values`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValue`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValues`.
