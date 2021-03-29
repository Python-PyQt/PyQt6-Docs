.. sip:method-description::
    :status: todo
    :pysig: 97ecfb6806202f6b76660508cd19022f
    :realsig: (const QSslKey&)
    :digest: 60da36d01f75460addc3532cd601c038

Sets the connection's private :sip:ref:`~PyQt6.QtNetwork.QSslKey` to *key*. The private key and the local :sip:ref:`~PyQt6.QtNetwork.QSslCertificate` are used by clients and servers that must prove their identity to SSL peers.

Both the key and the local certificate are required if you are creating an SSL server socket. If you are creating an SSL client socket, the key and local certificate are required if your client must identify itself to an SSL server.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.privateKey`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setLocalCertificate`.
