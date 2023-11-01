.. sip:method-description::
    :status: todo
    :pysig: b45133b575b7b933b47c94ed7949068e
    :realsig: (const QString&, QSsl::KeyAlgorithm, QSsl::EncodingFormat, const QByteArray&)
    :digest: 82145043d432daabce8fb104a7008608

This is an overloaded function.

Reads the string in file *fileName* and decodes it using a specified *algorithm* and encoding *format* to construct an :sip:ref:`~PyQt6.QtNetwork.QSslKey`. If the encoded key is encrypted, *passPhrase* is used to decrypt it.

The socket's private key is set to the constructed key. The private key and the local :sip:ref:`~PyQt6.QtNetwork.QSslCertificate` are used by clients and servers that must prove their identity to SSL peers.

Both the key and the local certificate are required if you are creating an SSL server socket. If you are creating an SSL client socket, the key and local certificate are required if your client must identify itself to an SSL server.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.privateKey`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setLocalCertificate`.
