.. sip:signal-description::
    :status: todo
    :pysig: 148ae2a993f284061b32799de36b298c
    :realsig: (QLocalSocket::LocalSocketError)
    :digest: 75b260fccebf6aef79965d0591f9878d

This signal is emitted after an error occurred. The *socketError* parameter describes the type of error that occurred.

:sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketError` is not a registered metatype, so for queued connections, you will have to register it with Q_DECLARE_METATYPE() and qRegisterMetaType().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.error`, errorString(), `Creating Custom Qt Types <https://doc.qt.io/qt-6/custom-types.html>`_.
