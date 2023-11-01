.. sip:method-description::
    :status: todo
    :pysig: d6044c74e95174c13ecde8f17b3bfb36
    :realsig: (const QString&, QSsl::SslProtocol)
    :digest: fb670e5d6d70882a757b816429b9f8d5

Constructs a :sip:ref:`~PyQt6.QtNetwork.QSslCipher` object for the cipher determined by *name* and *protocol*. The constructor accepts only supported ciphers (i.e., the *name* and *protocol* must identify a cipher in the list of ciphers returned by QSslSocket::supportedCiphers()).

You can call :sip:ref:`~PyQt6.QtNetwork.QSslCipher.isNull` after construction to check if *name* and *protocol* correctly identified a supported cipher.
