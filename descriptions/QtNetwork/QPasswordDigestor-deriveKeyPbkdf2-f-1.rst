.. sip:method-description::
    :status: todo
    :pysig: 19c2e9290b2283f5e1859c8ad180f30b
    :realsig: (QCryptographicHash::Algorithm, const QByteArray&, const QByteArray&, int, quint64)
    :digest: 33fd83768fed4ba2ea4a3dc7d5b3b659

Derive a key using the PBKDF2-algorithm as defined in RFC 8018, section 5.2.

This function takes the *data* and *salt*, and then applies HMAC-X, where the X is *algorithm*, repeatedly. It internally concatenates intermediate results to the final output until at least *dkLen* amount of bytes have been computed and it will execute HMAC-X *iterations* times each time a concatenation is required. The total number of times it will execute HMAC-X depends on *iterations*, *dkLen* and *algorithm* and can be calculated as ``iterations \* ceil(dkLen / QCryptographicHash::hashLength(algorithm))``.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QPasswordDigestor.deriveKeyPbkdf1`, :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode`, :sip:ref:`~PyQt6.QtCore.QCryptographicHash`.
