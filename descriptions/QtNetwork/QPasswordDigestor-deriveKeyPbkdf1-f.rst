.. sip:method-description::
    :status: todo
    :pysig: 120b2f5aa8876e74ec25403045444e84
    :realsig: (QCryptographicHash::Algorithm,const QByteArray&,const QByteArray&,int,quint64)
    :digest: aadc5ba558733e1c5861fe5568086b7e

Returns a hash computed using the PBKDF1-algorithm as defined in `RFC 8018 <https://tools.ietf.org/html/rfc8018#section-5.1>`_.

The function takes the *data* and *salt*, and then hashes it repeatedly for *iterations* iterations using the specified hash *algorithm*. If the resulting hash is longer than *dkLen* then it is truncated before it is returned.

This function only supports SHA-1 and MD5! The max output size is 160 bits (20 bytes) when using SHA-1, or 128 bits (16 bytes) when using MD5. Specifying a value for *dkLen* which is greater than this results in a warning and an empty :sip:ref:`~PyQt6.QtCore.QByteArray` is returned. To programmatically check this limit you can use :sip:ref:`~PyQt6.QtCore.QCryptographicHash.hashLength`. Furthermore: the *salt* must always be 8 bytes long!

**Note:** This function is provided for use with legacy applications and all new applications are recommended to use :sip:ref:`~PyQt6.QtNetwork.QPasswordDigestor.deriveKeyPbkdf2`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QPasswordDigestor.deriveKeyPbkdf2`, :sip:ref:`~PyQt6.QtCore.QCryptographicHash`, :sip:ref:`~PyQt6.QtCore.QCryptographicHash.hashLength`.
