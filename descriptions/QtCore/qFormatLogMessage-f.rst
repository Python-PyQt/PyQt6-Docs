.. sip:method-description::
    :status: todo
    :pysig: 7b957f1ce2b4785593ac02e4b49ff8f9
    :realsig: (QtMsgType,const QMessageLogContext&,const QString&)
    :digest: d893a529ad72de1901941765926854fa

Generates a formatted string out of the *type*, *context*, *str* arguments.

returns a QString that is formatted according to the current message pattern. It can be used by custom message handlers to format output similar to Qt's default message handler.

The function is thread-safe.

.. seealso:: :sip:ref:`~PyQt6.QtCore.qInstallMessageHandler`, :sip:ref:`~PyQt6.QtCore.qSetMessagePattern`.
