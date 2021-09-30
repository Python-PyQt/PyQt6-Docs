.. sip:method-description::
    :status: todo
    :pysig: 2427dc37299a8013ed5dbc92ca506bb7
    :realsig: (const QString&,QWebSocketProtocol::Version,QObject*)
    :digest: af9911f1559fce7b14442430101149cd

Creates a new :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` with the given *origin*, the *version* of the protocol to use and *parent*.

The *origin* of the client is as specified in `RFC 6454 <https://doc.qt.io/qt-6/https://datatracker.ietf.org/doc/html/rfc6454>`_. (The *origin* is not required for non-web browser clients (see `RFC 6455 <https://doc.qt.io/qt-6/https://datatracker.ietf.org/doc/html/rfc6455>`_)). The *origin* may not contain new line characters, otherwise the connection will be aborted immediately during the handshake phase.

**Note:** Currently only V13 (`RFC 6455 <https://doc.qt.io/qt-6/https://datatracker.ietf.org/doc/html/rfc6455>`_) is supported
