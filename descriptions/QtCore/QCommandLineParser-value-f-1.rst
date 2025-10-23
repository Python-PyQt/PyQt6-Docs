.. sip:method-description::
    :status: todo
    :pysig: 5402d751fcfc9eb84a404214f47473b4
    :realsig: (const QCommandLineOption&) const
    :digest: 405b7b18246b43fb483c8b741b8482db

Returns the option value found for the given *option*, or an empty string if not found.

For options found by the parser, the last value found for that option is returned. If the option wasn't specified on the command line, the default value is returned.

An empty string is returned if the option does not take a value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser.values`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValue`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValues`.
