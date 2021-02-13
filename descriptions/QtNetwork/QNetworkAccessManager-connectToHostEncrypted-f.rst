.. sip:method-description::
    :status: todo
    :pysig: 5dad7a2d5417e90f03bca4ae98e951cc
    :realsig: (const QString&,quint16,const QSslConfiguration&)
    :digest: 966e7fdd4cc12c04c998ef03691817db

Initiates a connection to the host given by *hostName* at port *port*, using *sslConfiguration*. This function is useful to complete the TCP and SSL handshake to a host before the HTTPS request is made, resulting in a lower network latency.

**Note:** Preconnecting a HTTP/2 connection can be done by calling setAllowedNextProtocols() on *sslConfiguration* with QSslConfiguration::ALPNProtocolHTTP2 contained in the list of allowed protocols. When using HTTP/2, one single connection per host is enough, i.e. calling this method multiple times per host will not result in faster network transactions.

**Note:** This function has no possibility to report errors.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.connectToHost`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.get`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.put`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.deleteResource`.
