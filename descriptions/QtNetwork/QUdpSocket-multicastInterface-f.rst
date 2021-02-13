.. sip:method-description::
    :status: todo
    :pysig: fb3f29ca19173c1bcf70419fc6444f2c
    :realsig: () const
    :digest: d4913b60f644cc19841e1b772b34b88f

Returns the interface for the outgoing interface for multicast datagrams. This corresponds to the IP_MULTICAST_IF socket option for IPv4 sockets and the IPV6_MULTICAST_IF socket option for IPv6 sockets. If no interface has been previously set, this function returns an invalid :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`. The socket must be in :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.BoundState`, otherwise an invalid :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.setMulticastInterface`.
