.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 153813ffc665dc5bf43fafb43a7477cb

Returns the maximum length, in bytes, of the PSK client identity.

**Note:** it is possible to set an identity whose length is greater than ; in this case, only the first  bytes will be actually sent to the server.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator.setIdentity`.
