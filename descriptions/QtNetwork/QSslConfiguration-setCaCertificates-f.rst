.. sip:method-description::
    :status: todo
    :pysig: be2a68d2d58d460f8dd22fecae06fa22
    :realsig: (const QList<QSslCertificate>&)
    :digest: 13601e53681c19aa58d81d87a156e7e7

Sets this socket's CA certificate database to be *certificates*. The certificate database must be set prior to the SSL handshake. The CA certificate database is used by the socket during the handshake phase to validate the peer's certificate.

**Note:** The default configuration uses the system CA certificate database. If that is not available (as is commonly the case on iOS), the default database is empty.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.caCertificates`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificates`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificate`.
