.. sip:method-description::
    :status: todo
    :pysig: c4ecc97fc8e3f5e3c19f192504413114
    :realsig: (const QByteArray&,QSsl::EncodingFormat)
    :digest: e823390059ff9e6b0dda133248cb9c54

Constructs a :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters` object using the byte array *encoded* in either PEM or DER form as specified by *encoding*.

Use the :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters.isValid` method on the returned object to check whether the Diffie-Hellman parameters were valid and loaded correctly.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters.isValid`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`.
