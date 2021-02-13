.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 8387362657c3caa10aab0d8aa50beb74

Sets the requested port number for the outgoing connection to be *port*. Valid values are 1 to 65535, or -1 to indicate that the remote port number is unknown.

The peer port number can also be used to indicate the expected port number of an incoming connection in the case of :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.UdpSocket` or :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.TcpServer` query types.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.peerPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.setPeerHostName`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.setLocalPort`.
