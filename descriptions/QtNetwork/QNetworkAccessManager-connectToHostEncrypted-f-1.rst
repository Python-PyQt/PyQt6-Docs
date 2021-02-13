.. sip:method-description::
    :status: todo
    :pysig: 50d85d97944f82125a8d0cb3e8453ce8
    :realsig: (const QString&,quint16,const QSslConfiguration&,const QString&)
    :digest: baf700f7e0d5e5e4034b4dbe9a38c1c3

This is an overloaded function.

Initiates a connection to the host given by *hostName* at port *port*, using *sslConfiguration* with *peerName* set to be the hostName used for certificate validation. This function is useful to complete the TCP and SSL handshake to a host before the HTTPS request is made, resulting in a lower network latency.

**Note:** Preconnecting a HTTP/2 connection can be done by calling setAllowedNextProtocols() on *sslConfiguration* with QSslConfiguration::ALPNProtocolHTTP2 contained in the list of allowed protocols. When using HTTP/2, one single connection per host is enough, i.e. calling this method multiple times per host will not result in faster network transactions.

**Note:** This function has no possibility to report errors.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.connectToHost`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.get`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.put`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.deleteResource`.
