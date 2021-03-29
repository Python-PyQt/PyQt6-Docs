.. sip:method-description::
    :status: todo
    :pysig: be2a68d2d58d460f8dd22fecae06fa22
    :realsig: (const QList<QSslCertificate>&)
    :digest: 48e568d86fce6618f78087f47b1c8e14

Sets the certificate chain to be presented to the peer during the SSL handshake to be *localChain*.

Setting the certificate chain once the connection has been established has no effect.

A certificate is the means of identification used in the SSL process. The local certificate is used by the remote end to verify the local user's identity against its list of Certification Authorities. In most cases, such as in HTTP web browsing, only servers identify to the clients, so the client does not send a certificate.

Unlike :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setLocalCertificate` this method allows you to specify any intermediate certificates required in order to validate your certificate. The first item in the list must be the leaf certificate.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.localCertificateChain`.
