.. sip:method-description::
    :status: todo
    :pysig: 540d03d543282018ff34d52a022e932e
    :realsig: (const QSslConfiguration&)
    :digest: 1ac62a9549dd59a5c0a89ba36d71a086

Sets the *sslConfiguration* to use for all following incoming connections.

This must be called before listen() to ensure that the desired configuration was in use during all handshakes.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslServer.sslConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setSslConfiguration`.
