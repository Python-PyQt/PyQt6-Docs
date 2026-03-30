.. sip:method-description::
    :status: todo
    :pysig: 2dc9975ecb681558b110f66995bc10e2
    :realsig: (const QByteArray&, QSsl::EncodingFormat)
    :digest: e823390059ff9e6b0dda133248cb9c54

Constructs a :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters` object using the byte array *encoded* in either PEM or DER form as specified by *encoding*.

Use the :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters.isValid` method on the returned object to check whether the Diffie-Hellman parameters were valid and loaded correctly.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters.isValid`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`.
