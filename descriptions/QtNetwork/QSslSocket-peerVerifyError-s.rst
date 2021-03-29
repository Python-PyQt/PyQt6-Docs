.. sip:signal-description::
    :status: todo
    :pysig: c7010c0e6ebee9ba24c31bb143132851
    :realsig: (const QSslError&)
    :digest: 630319feec8e86241b11e0fa30d29808

:sip:ref:`~PyQt6.QtNetwork.QSslSocket` can emit this signal several times during the SSL handshake, before encryption has been established, to indicate that an error has occurred while establishing the identity of the peer. The *error* is usually an indication that :sip:ref:`~PyQt6.QtNetwork.QSslSocket` is unable to securely identify the peer.

This signal provides you with an early indication when something's wrong. By connecting to this signal, you can manually choose to tear down the connection from inside the connected slot before the handshake has completed. If no action is taken, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` will proceed to emitting :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors`.
