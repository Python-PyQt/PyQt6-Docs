.. sip:method-description::
    :status: todo
    :pysig: be2a68d2d58d460f8dd22fecae06fa22
    :realsig: (const QList<QSslCertificate>&)
    :digest: 7a3a5e364daa40246cfc1ef24ab3bbf6

Adds *certificates* to this configuration's CA certificate database. The certificate database must be set prior to the SSL handshake. The CA certificate database is used by the socket during the handshake phase to validate the peer's certificate.

**Note:** The default configuration uses the system CA certificate database. If that is not available (as is commonly the case on iOS), the default database is empty.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.caCertificates`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCaCertificates`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificate`.
