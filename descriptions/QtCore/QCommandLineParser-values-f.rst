.. sip:method-description::
    :status: todo
    :pysig: 44749fd150362d078dc16c6fe99ad605
    :realsig: (const QString&) const
    :digest: ea0f0f578058635b5ba9e3eb758892a5

Returns a list of option values found for the given option name *optionName*, or an empty list if not found.

The name provided can be any long or short name of any option that was added with :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addOption`. All the options names are treated as being equivalent. If the name is not recognized or that option was not present, an empty list is returned.

For options found by the parser, the list will contain an entry for each time the option was encountered by the parser. If the option wasn't specified on the command line, the default values are returned.

An empty list is returned if the option does not take a value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser.value`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValue`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValues`.
