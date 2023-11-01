.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&) const
    :digest: abce65cd604dbbb75010e51a542ac318

Checks whether the option *name* was passed to the application.

Returns ``true`` if the option *name* was set, false otherwise.

The name provided can be any long or short name of any option that was added with :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addOption`. All the options names are treated as being equivalent. If the name is not recognized or that option was not present, false is returned.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineparser.py
    :lines: 61-61
