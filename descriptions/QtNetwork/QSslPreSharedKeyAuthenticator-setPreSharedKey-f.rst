.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: a40d2bd5d6cab78eb27bbf50b6f8b117

Sets the pre shared key to *preSharedKey*.

**Note:** it is possible to set a key whose length is greater than the :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator.maximumPreSharedKeyLength`; in this case, only the first :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator.maximumPreSharedKeyLength` bytes will be actually sent to the server.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator.preSharedKey`, :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator.maximumPreSharedKeyLength`, :sip:ref:`~PyQt6.QtCore.QByteArray.fromHex`.
