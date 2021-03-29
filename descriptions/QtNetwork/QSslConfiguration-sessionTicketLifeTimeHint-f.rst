.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: f288c4651636a52de33cacd93fa70f7d

If :sip:ref:`~PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableSessionPersistence` was turned off, this function returns the session ticket life time hint sent by the server (which might be 0). If the server did not send a session ticket (e.g. when resuming a session or when the server does not support it) or :sip:ref:`~PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableSessionPersistence` was not turned off, this function returns -1.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.sessionTicket`, :sip:ref:`~PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableSessionPersistence`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setSslOption`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.newSessionTicketReceived`.
