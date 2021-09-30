.. sip:signal-description::
    :status: todo
    :pysig: c7010c0e6ebee9ba24c31bb143132851
    :realsig: (const QSslError&)
    :digest: 899fb1d11d8e970090b8a70c77f28a67

:sip:ref:`~PyQt6.QtWebSockets.QWebSocket` emits this signal if a certificate verification error was found and if early error reporting was enabled in :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`. An application is expected to inspect the *error* and decide if it wants to continue the handshake, or abort it and send an alert message to the peer. The signal-slot connection must be direct.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.continueInterruptedHandshake`, :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setHandshakeMustInterruptOnError`.
