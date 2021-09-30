.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: 83bfe50197a6f30d22e6f7fc97e831fb

This signal is emitted every time a payload of data has been written to the socket. The *bytes* argument is set to the number of bytes that were written in this payload.

**Note:** This signal has the same meaning both for secure and non-secure WebSockets. As opposed to :sip:ref:`~PyQt6.QtNetwork.QSslSocket`,  is only emitted when encrypted data is effectively written (see :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encryptedBytesWritten`).

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.close`.
