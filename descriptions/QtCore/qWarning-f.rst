.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const char*)
    :digest: 99e9ee13b5d757e377058f4c1c2d8d80

Calls the message handler with the warning message *message*. If no message handler has been installed, the message is printed to stderr. Under Windows, the message is sent to the debugger. On QNX the message is sent to slogger2. This function does nothing if ``QT_NO_WARNING_OUTPUT`` was defined during compilation; it exits if at the nth warning corresponding to the counter in environment variable ``QT_FATAL_WARNINGS``. That is, if the environment variable contains the value 1, it will exit on the 1st message; if it contains the value 10, it will exit on the 10th message. Any non-numeric value is equivalent to 1.

This function takes a format string and a list of arguments, similar to the C printf() function. The format should be a Latin-1 string.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 335-339

If you include <QtDebug>, a more convenient syntax is also available:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 344-345

This syntax inserts a space between each item, and appends a newline at the end.

To suppress the output at runtime, install your own message handler with :sip:ref:`~PyQt6.QtCore.qInstallMessageHandler`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.qDebug`, :sip:ref:`~PyQt6.QtCore.qInfo`, :sip:ref:`~PyQt6.QtCore.qCritical`, :sip:ref:`~PyQt6.QtCore.qFatal`, :sip:ref:`~PyQt6.QtCore.qInstallMessageHandler`.
