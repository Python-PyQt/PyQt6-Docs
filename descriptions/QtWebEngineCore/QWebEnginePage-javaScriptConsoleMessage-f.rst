.. sip:method-description::
    :status: todo
    :pysig: 8d782335b5af4be123aa8ecf56eb36e8
    :realsig: (QWebEnginePage::JavaScriptConsoleMessageLevel,const QString&,int,const QString&)
    :digest: ce8f21f0c715e25016d0410ca4741553

This function is called when a JavaScript program tries to print the *message* to the web browser's console.

For example, in case of evaluation errors the source URL may be provided in *sourceID* as well as the *lineNumber*.

*level* indicates the severity of the event that triggered the message. That is, whether it was triggered by an error or a less severe event.

Since Qt 5.6, the default implementation logs the messages in a ``js`` :sip:ref:`~PyQt6.QtCore.QLoggingCategory`.

.. seealso:: `Console Logging <https://doc.qt.io/qt-6/qtwebengine-debugging.html#console-logging>`_.
