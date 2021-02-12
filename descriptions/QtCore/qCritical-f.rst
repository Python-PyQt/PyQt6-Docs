.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const char*)
    :digest: 80828a371b96d803353926ef92ed45a9

Calls the message handler with the critical message *message*. If no message handler has been installed, the message is printed to stderr. Under Windows, the message is sent to the debugger. On QNX the message is sent to slogger2.

It exits if the environment variable QT_FATAL_CRITICALS is not empty.

This function takes a format string and a list of arguments, similar to the C printf() function. The format should be a Latin-1 string.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 350-355

If you include <QtDebug>, a more convenient syntax is also available:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 360-361

A space is inserted between the items, and a newline is appended at the end.

To suppress the output at runtime, install your own message handler with :sip:ref:`~PyQt6.QtCore.qInstallMessageHandler`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.qDebug`, :sip:ref:`~PyQt6.QtCore.qInfo`, :sip:ref:`~PyQt6.QtCore.qWarning`, :sip:ref:`~PyQt6.QtCore.qFatal`, :sip:ref:`~PyQt6.QtCore.qInstallMessageHandler`.
