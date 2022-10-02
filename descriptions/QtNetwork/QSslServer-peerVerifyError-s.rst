.. sip:signal-description::
    :status: todo
    :pysig: 9c2c3f54d13a32f7bd66703277337bdf
    :realsig: (QSslSocket*,const QSslError&)
    :digest: 8d3c2862423051906357d8b79732ed3a

:sip:ref:`~PyQt6.QtNetwork.QSslServer` can emit this signal several times during the SSL handshake, before encryption has been established, to indicate that an error has occurred while establishing the identity of the peer. The *error* is usually an indication that *socket* is unable to securely identify the peer.

This signal provides you with an early indication when something's wrong. By connecting to this signal, you can manually choose to tear down the connection from inside the connected slot before the handshake has completed. If no action is taken, :sip:ref:`~PyQt6.QtNetwork.QSslServer` will proceed to emitting :sip:ref:`~PyQt6.QtNetwork.QSslServer.sslErrors`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslServer.sslErrors`.
