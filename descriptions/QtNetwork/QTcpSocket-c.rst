.. sip:class-description::
    :status: todo
    :brief: TCP socket
    :digest: 38a95a90b5c769c6af982b8619722de5

The :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` class provides a TCP socket.

TCP (Transmission Control Protocol) is a reliable, stream-oriented, connection-oriented transport protocol. It is especially well suited for continuous transmission of data.

:sip:ref:`~PyQt6.QtNetwork.QTcpSocket` is a convenience subclass of :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` that allows you to establish a TCP connection and transfer streams of data. See the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` documentation for details.

**Note:** TCP sockets cannot be opened in QIODevice::Unbuffered mode.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QTcpServer`, :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`, `Fortune Server Example <https://doc.qt.io/qt-6/qtnetwork-fortuneserver-example.html>`_, `Fortune Client Example <https://doc.qt.io/qt-6/qtnetwork-fortuneclient-example.html>`_, `Threaded Fortune Server Example <https://doc.qt.io/qt-6/qtnetwork-threadedfortuneserver-example.html>`_, `Blocking Fortune Client Example <https://doc.qt.io/qt-6/qtnetwork-blockingfortuneclient-example.html>`_, `Loopback Example <https://doc.qt.io/qt-6/qtnetwork-loopback-example.html>`_, `Torrent Example <https://doc.qt.io/qt-6/qtnetwork-torrent-example.html>`_.
