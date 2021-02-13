.. sip:method-description::
    :status: todo
    :pysig: 120b2f5aa8876e74ec25403045444e84
    :realsig: (QCryptographicHash::Algorithm,const QByteArray&,const QByteArray&,int,quint64)
    :digest: 20c8f4a050765a36933bfe05c829185a

Derive a key using the PBKDF2-algorithm as defined in `RFC 8018 <https://tools.ietf.org/html/rfc8018#section-5.2>`_.

This function takes the *data* and *salt*, and then applies HMAC-X, where the X is *algorithm*, repeatedly. It internally concatenates intermediate results to the final output until at least *dkLen* amount of bytes have been computed and it will execute HMAC-X *iterations* times each time a concatenation is required. The total number of times it will execute HMAC-X depends on *iterations*, *dkLen* and *algorithm* and can be calculated as ``iterations \* ceil(dkLen / QCryptographicHash::hashLength(algorithm))``.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QPasswordDigestor.deriveKeyPbkdf1`, :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode`, :sip:ref:`~PyQt6.QtCore.QCryptographicHash`.
