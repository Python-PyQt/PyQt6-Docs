.. sip:signal-description::
    :status: todo
    :pysig: d66ab6bfd37177778529d948c61ba8a0
    :realsig: (QAbstractSocket::SocketError)
    :digest: bc1ac08eda8f677396b9d123ca784eeb

This signal is emitted after an error occurred. The *socketError* parameter describes the type of error that occurred.

When this signal is emitted, the socket may not be ready for a reconnect attempt. In that case, attempts to reconnect should be done from the event loop. For example, use a :sip:ref:`~PyQt6.QtCore.QTimer.singleShot` with 0 as the timeout.

:sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError` is not a registered metatype, so for queued connections, you will have to register it with Q_DECLARE_METATYPE() and qRegisterMetaType().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.error`, errorString(), `Creating Custom Qt Types <https://doc.qt.io/qt-6/custom-types.html>`_.
