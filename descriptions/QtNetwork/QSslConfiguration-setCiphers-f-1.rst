.. sip:method-description::
    :status: todo
    :pysig: b4e94c82137ea8b86f10751916e7fc22
    :realsig: (const QList<QSslCipher>&)
    :digest: 1a0c8e6d32789c113798f1cbaa335140

Sets the cryptographic cipher suite for this socket to *ciphers*, which must contain a subset of the ciphers in the list returned by :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedCiphers`.

Restricting the cipher suite must be done before the handshake phase, where the session cipher is chosen.

**Note:** This is not currently supported in the Schannel backend.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.ciphers`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.supportedCiphers`.
