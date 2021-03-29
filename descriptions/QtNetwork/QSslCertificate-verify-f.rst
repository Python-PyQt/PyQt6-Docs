.. sip:method-description::
    :status: todo
    :pysig: ed41a8687aa05cd41ef668abe2974440
    :realsig: (const QList<QSslCertificate>&,const QString&)
    :digest: 9a1322f8b1c36b41080883c0adbd9760

Verifies a certificate chain. The chain to be verified is passed in the *certificateChain* parameter. The first certificate in the list should be the leaf certificate of the chain to be verified. If *hostName* is specified then the certificate is also checked to see if it is valid for the specified host name.

Note that the root (CA) certificate should not be included in the list to be verified, this will be looked up automatically using the CA list specified in the default :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`, and, in addition, if possible, CA certificates loaded on demand on Unix and Windows.
