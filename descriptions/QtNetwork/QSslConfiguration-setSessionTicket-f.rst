.. sip:method-description::
    :status: todo
    :pysig: c70916e782d9742b90f37ccdedc4f900
    :realsig: (const QByteArray&)
    :digest: 70f1e43d630e950d44805c72ee511218

Sets the session ticket to be used in an SSL handshake. :sip:ref:`~PyQt6.QtNetwork.QSsl.SslOption.SslOptionDisableSessionPersistence` must be turned off for this to work, and *sessionTicket* must be in ASN.1 format as returned by :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.sessionTicket`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.sessionTicket`, :sip:ref:`~PyQt6.QtNetwork.QSsl.SslOption.SslOptionDisableSessionPersistence`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setSslOption`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.newSessionTicketReceived`.
