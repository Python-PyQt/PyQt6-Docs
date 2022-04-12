.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const char*)
    :digest: 0d0ed4e1428a6cfbadc779f246f990bb

Calls the message handler with the informational message *message*. If no message handler has been installed, the message is printed to stderr. Under Windows, the message is sent to the console, if it is a console application; otherwise, it is sent to the debugger. On QNX the message is sent to slogger2. This function does nothing if ``QT_NO_INFO_OUTPUT`` was defined during compilation.

If you pass the function a format string and a list of arguments, it works in similar way to the C printf() function. The format should be a Latin-1 string.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 327-327

If you include ``<QtDebug>``, a more convenient syntax is also available:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 331-331

With this syntax, the function returns a QDebug object that is configured to use the :sip:ref:`~PyQt6.QtCore.QtMsgType.QtInfoMsg` message type. It automatically puts a single space between each item, and outputs a newline at the end. It supports many C++ and Qt types.

To suppress the output at runtime, install your own message handler using :sip:ref:`~PyQt6.QtCore.qInstallMessageHandler`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.qDebug`, :sip:ref:`~PyQt6.QtCore.qWarning`, :sip:ref:`~PyQt6.QtCore.qCritical`, :sip:ref:`~PyQt6.QtCore.qFatal`, :sip:ref:`~PyQt6.QtCore.qInstallMessageHandler`.
