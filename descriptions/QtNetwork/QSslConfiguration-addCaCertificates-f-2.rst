.. sip:method-description::
    :status: todo
    :pysig: 4d255c4fc122134e2180bc7663109c32
    :realsig: (const QString&, QSsl::EncodingFormat, QSslCertificate::PatternSyntax)
    :digest: 22d6163341ce5321c70449f20278e6b5

Searches all files in the *path* for certificates encoded in the specified *format* and adds them to this socket's CA certificate database. *path* must be a file or a pattern matching one or more files, as specified by *syntax*. Returns ``true`` if one or more certificates are added to the socket's CA certificate database; otherwise returns ``false``.

The CA certificate database is used by the socket during the handshake phase to validate the peer's certificate.

For more precise control, use :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificate`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificate`, :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.fromPath`.
