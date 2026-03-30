.. sip:method-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: 82d8bfb1d7e15aac69adac13462b162c

Constructs a :sip:ref:`~PyQt6.QtNetwork.QSslCipher` object for the cipher determined by *name*. The constructor accepts only supported ciphers (i.e., the *name* must identify a cipher in the list of ciphers returned by QSslSocket::supportedCiphers()).

You can call :sip:ref:`~PyQt6.QtNetwork.QSslCipher.isNull` after construction to check if *name* correctly identified a supported cipher.
