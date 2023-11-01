.. sip:method-description::
    :status: todo
    :pysig: 8f48478791d03642797fb4455d9c598c
    :realsig: ()
    :digest: 6e2f552324bf22d3209c19cfdf2db1e8

Adds help options to the command-line parser.

The options specified for this command-line are described by ``-h`` or ``--help``. On Windows, the alternative ``-?`` is also supported. The option ``--help-all`` extends that to include generic Qt options, not defined by this command, in the output.

These options are handled automatically by :sip:ref:`~PyQt6.QtCore.QCommandLineParser`.

Remember to use :sip:ref:`~PyQt6.QtCore.QCommandLineParser.setApplicationDescription` to set the application description, which will be displayed when this option is used.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineparser_main.py
    :lines: 56-95

Returns the option instance, which can be used to call :sip:ref:`~PyQt6.QtCore.QCommandLineParser.isSet`.
