.. sip:method-description::
    :status: todo
    :pysig: 52a75f181d42d8874cf764264b03b939
    :realsig: (QWebEnginePage::JavaScriptConsoleMessageLevel, const QString&, int, const QString&)
    :digest: 5f27308c6de957228273f6739418d7d5

This function is called when a JavaScript program tries to print the *message* to the web browser's console.

For example, in case of evaluation errors the source URL may be provided in *sourceID* as well as the *lineNumber*.

*level* indicates the severity of the event that triggered the message. That is, whether it was triggered by an error or a less severe event.

The default implementation logs the messages in a ``js`` :sip:ref:`~PyQt6.QtCore.QLoggingCategory`.

.. seealso:: `Console Logging <https://doc.qt.io/qt-6/qtwebengine-debugging.html#console-logging>`_.
