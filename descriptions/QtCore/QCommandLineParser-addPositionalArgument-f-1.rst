.. sip:method-description::
    :status: todo
    :pysig: b146c93ad8bcabb4ad9f93c50e6bf7dd
    :realsig: (const QString&, const QString&, const QString&)
    :digest: bccda1809edb785141c0d83b8bd67cfc

Defines an additional argument to the application, for the benefit of the help text.

The argument *name* and *description* will appear under the ``Arguments:`` section of the help. If *syntax* is specified, it will be appended to the Usage line, otherwise the *name* will be appended.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineparser.py
    :lines: 79-97

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addHelpOption`, :sip:ref:`~PyQt6.QtCore.QCommandLineParser.helpText`.
