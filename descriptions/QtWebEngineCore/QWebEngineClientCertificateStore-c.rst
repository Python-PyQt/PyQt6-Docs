.. sip:class-description::
    :status: todo
    :brief: In-memory store for client certificates
    :digest: afdb616517bab8889104f0c7239b2754

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientCertificateStore` class provides an in-memory store for client certificates.

The class allows to store client certificates in an in-memory store. When a web site requests an SSL client certificate, the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.selectClientCertificate` signal is emitted with matching certificates from the native certificate store or the in-memory store.

The class instance can be obtained with the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.clientCertificateStore` method.

::

    QFile certFile(":/resources/certificate.crt");
    certFile.open(QIODevice::ReadOnly);
    const QSslCertificate cert(certFile.readAll(), QSsl::Pem);

    QFile keyFile(":/resources/privatekey.key");
    keyFile.open(QIODevice::ReadOnly);
    const QSslKey sslKey(keyFile.readAll(), QSsl::Rsa, QSsl::Pem, QSsl::PrivateKey, "");

    QWebEngineProfile profile;
    profile.clientCertificateStore()->add(cert, sslKey);
