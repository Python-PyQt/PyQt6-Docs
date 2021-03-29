.. sip:class-description::
    :status: todo
    :brief: Additional information about a log message
    :digest: 7d123fcfb681b126a38a4a580705fee4

The :sip:ref:`~PyQt6.QtCore.QMessageLogContext` class provides additional information about a log message.

The class provides information about the source code location a :sip:ref:`~PyQt6.QtCore.qDebug`, :sip:ref:`~PyQt6.QtCore.qInfo`, :sip:ref:`~PyQt6.QtCore.qWarning`, :sip:ref:`~PyQt6.QtCore.qCritical` or :sip:ref:`~PyQt6.QtCore.qFatal` message was generated.

**Note:** By default, this information is recorded only in debug builds. You can overwrite this explicitly by defining ``QT_MESSAGELOGCONTEXT`` or ``QT_NO_MESSAGELOGCONTEXT``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMessageLogger`, QtMessageHandler, :sip:ref:`~PyQt6.QtCore.qInstallMessageHandler`.
