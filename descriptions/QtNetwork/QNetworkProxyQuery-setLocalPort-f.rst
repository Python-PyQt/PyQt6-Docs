.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: ccba659dba34282c8e6ab50cdf78b763

Sets the port number that the socket wishes to use locally to accept incoming packets from remote servers to *port*. The local port is most often used with the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.TcpServer` and :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.UdpSocket` query types.

Valid values are 0 to 65535 (with 0 indicating that any port number will be acceptable) or -1, which means the local port number is unknown or not applicable.

In some circumstances, for special protocols, it's the local port number can also be used with a query of type :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.TcpSocket`. When that happens, the socket is indicating it wishes to use the port number *port* when connecting to a remote host.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.localPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.setPeerPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.setPeerHostName`.
