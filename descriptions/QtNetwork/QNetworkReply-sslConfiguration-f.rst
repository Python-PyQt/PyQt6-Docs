.. sip:method-description::
    :status: todo
    :pysig: 540d03d543282018ff34d52a022e932e
    :realsig: () const
    :digest: fc0e66b8b87cf1e1538c65e094d13941

Returns the SSL configuration and state associated with this reply, if SSL was used. It will contain the remote server's certificate, its certificate chain leading to the Certificate Authority as well as the encryption ciphers in use.

The peer's certificate and its certificate chain will be known by the time :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslErrors` is emitted, if it's emitted.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.setSslConfiguration`.
