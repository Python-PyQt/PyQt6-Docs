.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: 8f3e7471c1825c916d397e87d4041938

Sets the PSK client identity (to be advised to the server) to *identity*.

**Note:** it is possible to set an identity whose length is greater than :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator.maximumIdentityLength`; in this case, only the first :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator.maximumIdentityLength` bytes will be actually sent to the server.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator.identity`, :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator.maximumIdentityLength`.
