.. sip:signal-description::
    :status: todo
    :pysig: c7010c0e6ebee9ba24c31bb143132851
    :realsig: (const QSslError&)
    :digest: 6f62783b658b8cf6fe06001677b374ea

:sip:ref:`~PyQt6.QtNetwork.QSslSocket` emits this signal if a certificate verification error was found and if early error reporting was enabled in :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`. An application is expected to inspect the *error* and decide if it wants to continue the handshake, or abort it and send an alert message to the peer. The signal-slot connection must be direct.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.continueInterruptedHandshake`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setHandshakeMustInterruptOnError`.
