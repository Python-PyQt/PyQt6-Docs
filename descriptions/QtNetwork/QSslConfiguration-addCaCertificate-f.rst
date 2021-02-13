.. sip:method-description::
    :status: todo
    :pysig: b3c432d61e79f3a1841b7e0cdc24270d
    :realsig: (const QSslCertificate&)
    :digest: a07f282bdf1112fbd84590516b9e4c14

Adds *certificate* to this configuration's CA certificate database. The certificate database must be set prior to the SSL handshake. The CA certificate database is used by the socket during the handshake phase to validate the peer's certificate.

**Note:** The default configuration uses the system CA certificate database. If that is not available (as is commonly the case on iOS), the default database is empty.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.caCertificates`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCaCertificates`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificates`.
