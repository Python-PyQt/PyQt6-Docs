.. sip:method-description::
    :status: todo
    :pysig: 54321f091b630b22acf3f94e5c82ad0a
    :realsig: () const
    :digest: 20fa1b10a63beec516c8ebb047fe55b5

Returns the socket's cryptographic :sip:ref:`~PyQt6.QtNetwork.QSslCipher`, or a null cipher if the connection isn't encrypted. The socket's cipher for the session is set during the handshake phase. The cipher is used to encrypt and decrypt data transmitted through the socket.

The SSL infrastructure also provides functions for setting the ordered list of ciphers from which the handshake phase will eventually select the session cipher. This ordered list must be in place before the handshake phase begins.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.ciphers`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCiphers`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedCiphers`.
