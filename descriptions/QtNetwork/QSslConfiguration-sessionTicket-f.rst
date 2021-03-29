.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 6a91a5198e6e43f3aa02c660cdb316d4

If :sip:ref:`~PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableSessionPersistence` was turned off, this function returns the session ticket used in the SSL handshake in ASN.1 format, suitable to e.g. be persisted to disk. If no session ticket was used or :sip:ref:`~PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableSessionPersistence` was not turned off, this function returns an empty :sip:ref:`~PyQt6.QtCore.QByteArray`.

**Note:** When persisting the session ticket to disk or similar, be careful not to expose the session to a potential attacker, as knowledge of the session allows for eavesdropping on data encrypted with the session parameters.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setSessionTicket`, :sip:ref:`~PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableSessionPersistence`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setSslOption`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.newSessionTicketReceived`.
