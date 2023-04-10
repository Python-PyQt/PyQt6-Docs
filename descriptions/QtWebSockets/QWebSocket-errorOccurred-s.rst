.. sip:signal-description::
    :status: todo
    :pysig: d66ab6bfd37177778529d948c61ba8a0
    :realsig: (QAbstractSocket::SocketError)
    :digest: 0726025f39ec12abb9fda7a5d2c2f089

This signal is emitted after an error occurred.

The *error* parameter describes the type of error that occurred.

:sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError` is not a registered metatype, so for queued connections, you will have to register it with Q_DECLARE_METATYPE() and qRegisterMetaType().

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.error`, :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.errorString`.
