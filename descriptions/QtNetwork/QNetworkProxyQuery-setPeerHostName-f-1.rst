.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 25a64420a347699fc98e936f8ff06ca7

Sets the hostname of the outgoing connection being requested to *hostname*. An empty hostname can be used to indicate that the remote host is unknown.

The peer host name can also be used to indicate the expected source address of an incoming connection in the case of :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.UdpSocket` or :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.TcpServer` query types.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.peerHostName`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.setPeerPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.setLocalPort`.
