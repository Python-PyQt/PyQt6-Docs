.. sip:method-description::
    :status: todo
    :pysig: c785931753a4b20ec255a1b98b3c5e01
    :realsig: (QIODevice*,QSsl::EncodingFormat)
    :digest: 64c3af7dd57b26e7cb59e4068c21a754

Constructs a :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters` object by reading from *device* in either PEM or DER form as specified by *encoding*.

Use the :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters.isValid` method on the returned object to check whether the Diffie-Hellman parameters were valid and loaded correctly.

In particular, if *device* is ``nullptr`` or not open for reading, an invalid object will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters.isValid`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`.
