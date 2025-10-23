.. sip:method-description::
    :status: todo
    :pysig: 2ab5b43723a5b7fbaed736fb0e508e8c
    :realsig: (const QCommandLineOption&) const
    :digest: d5f7d323d81178993e5dcad4bb4a11a2

Returns a list of option values found for the given *option*, or an empty list if not found.

For options found by the parser, the list will contain an entry for each time the option was encountered by the parser. If the option wasn't specified on the command line, the default values are returned.

An empty list is returned if the option does not take a value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser.value`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValue`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValues`.
