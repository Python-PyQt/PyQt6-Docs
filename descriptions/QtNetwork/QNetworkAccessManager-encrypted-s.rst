.. sip:signal-description::
    :status: todo
    :pysig: 63e26fb998d1a16ab1cdaed04a236ca7
    :realsig: (QNetworkReply*)
    :digest: 2c7ff5df4afe7664f8ee04b65e71be7b

This signal is emitted when an SSL/TLS session has successfully completed the initial handshake. At this point, no user data has been transmitted. The signal can be used to perform additional checks on the certificate chain, for example to notify users when the certificate for a website has changed. The *reply* parameter specifies which network reply is responsible. If the reply does not match the expected criteria then it should be aborted by calling :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.abort` by a slot connected to this signal. The SSL configuration in use can be inspected using the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.sslConfiguration` method.

Internally, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` may open multiple connections to a server, in order to allow it process requests in parallel. These connections may be reused, which means that the  signal would not be emitted. This means that you are only guaranteed to receive this signal for the first connection to a site in the lifespan of the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encrypted`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.encrypted`.
