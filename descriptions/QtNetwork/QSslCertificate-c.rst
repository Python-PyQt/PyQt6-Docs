.. sip:class-description::
    :status: todo
    :brief: Convenient API for an X509 certificate
    :digest: 8cd1edcae4fb7248303d34d68848325d

The :sip:ref:`~PyQt6.QtNetwork.QSslCertificate` class provides a convenient API for an X509 certificate.

:sip:ref:`~PyQt6.QtNetwork.QSslCertificate` stores an X509 certificate, and is commonly used to verify the identity and store information about the local host, a remotely connected peer, or a trusted third party Certificate Authority.

There are many ways to construct a :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`. The most common way is to call :sip:ref:`~PyQt6.QtNetwork.QSslSocket.peerCertificate`, which returns a :sip:ref:`~PyQt6.QtNetwork.QSslCertificate` object, or :sip:ref:`~PyQt6.QtNetwork.QSslSocket.peerCertificateChain`, which returns a list of them. You can also load certificates from a DER (binary) or PEM (Base64) encoded bundle, typically stored as one or more local files, or in a Qt Resource.

You can call :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.isNull` to check if your certificate is null. By default, :sip:ref:`~PyQt6.QtNetwork.QSslCertificate` constructs a null certificate. A null certificate is invalid, but an invalid certificate is not necessarily null. If you want to reset all contents in a certificate, call :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.clear`.

After loading a certificate, you can find information about the certificate, its subject, and its issuer, by calling one of the many accessor functions, including :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.version`, :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.serialNumber`, :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.issuerInfo` and :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.subjectInfo`. You can call :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.effectiveDate` and :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.expiryDate` to check when the certificate starts being effective and when it expires. The :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.publicKey` function returns the certificate subject's public key as a :sip:ref:`~PyQt6.QtNetwork.QSslKey`. You can call :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.issuerInfo` or :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.subjectInfo` to get detailed information about the certificate issuer and its subject.

Internally, :sip:ref:`~PyQt6.QtNetwork.QSslCertificate` is stored as an X509 structure. You can access this handle by calling :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.handle`, but the results are likely to not be portable.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket`, :sip:ref:`~PyQt6.QtNetwork.QSslKey`, :sip:ref:`~PyQt6.QtNetwork.QSslCipher`, :sip:ref:`~PyQt6.QtNetwork.QSslError`.
