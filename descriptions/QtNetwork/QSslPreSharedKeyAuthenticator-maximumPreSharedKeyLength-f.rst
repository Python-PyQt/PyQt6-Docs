.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: ad037b92fd3d05d2ff33e711a888dc21

Returns the maximum length, in bytes, of the pre shared key.

**Note:** it is possible to set a key whose length is greater than the ; in this case, only the first  bytes will be actually sent to the server.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator.setPreSharedKey`.
