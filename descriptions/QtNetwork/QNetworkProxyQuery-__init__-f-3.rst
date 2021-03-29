.. sip:method-description::
    :status: todo
    :pysig: 95d0c2ac2de704e5f36e992960fe0951
    :realsig: (quint16,const QString&,QNetworkProxyQuery::QueryType)
    :digest: 28ce4c29e30d058b18f503a2d7d286fd

Constructs a :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery` of type *queryType* and sets the protocol tag to be *protocolTag*. This constructor is suitable for :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.TcpSocket` queries because it sets the local port number to *bindPort*.

Note that *bindPort* is of type quint16 to indicate the exact port number that is requested. The value of -1 (unknown) is not allowed in this context.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.localPort`.
