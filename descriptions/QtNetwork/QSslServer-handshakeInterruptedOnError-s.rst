.. sip:signal-description::
    :status: todo
    :pysig: 9c2c3f54d13a32f7bd66703277337bdf
    :realsig: (QSslSocket*,const QSslError&)
    :digest: 50d3d08723bc88258842f64dfce0c760

:sip:ref:`~PyQt6.QtNetwork.QSslServer` emits this signal if a certificate verification error was found by *socket* and if early error reporting was enabled in :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`. An application is expected to inspect the *error* and decide if it wants to continue the handshake, or abort it and send an alert message to the peer. The signal-slot connection must be direct.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.continueInterruptedHandshake`, :sip:ref:`~PyQt6.QtNetwork.QSslServer.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setHandshakeMustInterruptOnError`.
