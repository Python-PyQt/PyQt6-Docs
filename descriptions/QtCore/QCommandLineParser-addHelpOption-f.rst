.. sip:method-description::
    :status: todo
    :pysig: 8f48478791d03642797fb4455d9c598c
    :realsig: ()
    :digest: 41002e2dd9798a15de45d7bfe5aac866

Adds the help option (``-h``, ``--help`` and ``-?`` on Windows) as well as an option ``--help-all`` to include Qt-specific options in the output.

These options are handled automatically by :sip:ref:`~PyQt6.QtCore.QCommandLineParser`.

Remember to use :sip:ref:`~PyQt6.QtCore.QCommandLineParser.setApplicationDescription` to set the application description, which will be displayed when this option is used.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineparser_main.py
    :lines: 56-95

Returns the option instance, which can be used to call :sip:ref:`~PyQt6.QtCore.QCommandLineParser.isSet`.
