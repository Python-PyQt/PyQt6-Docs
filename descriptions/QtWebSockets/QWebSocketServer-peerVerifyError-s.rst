.. sip:signal-description::
    :status: todo
    :pysig: c7010c0e6ebee9ba24c31bb143132851
    :realsig: (const QSslError&)
    :digest: 4cde86e2ee8adabfd6a36a05b2b860b5

:sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` can emit this signal several times during the SSL handshake, before encryption has been established, to indicate that an error has occurred while establishing the identity of the peer. The *error* is usually an indication that :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` is unable to securely identify the peer.

This signal provides you with an early indication when something is wrong. By connecting to this signal, you can manually choose to tear down the connection from inside the connected slot before the handshake has completed. If no action is taken, :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` will proceed to emitting :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.sslErrors`.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.sslErrors`.
