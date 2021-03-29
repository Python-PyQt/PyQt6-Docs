.. sip:method-description::
    :status: todo
    :pysig: fb3f29ca19173c1bcf70419fc6444f2c
    :realsig: (const QNetworkInterface&)
    :digest: 7346bbf40220bd356b1e7ff10c65cfb7

Sets the outgoing interface for multicast datagrams to the interface *iface*. This corresponds to the IP_MULTICAST_IF socket option for IPv4 sockets and the IPV6_MULTICAST_IF socket option for IPv6 sockets. The socket must be in :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.BoundState`, otherwise this function does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.multicastInterface`, :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.joinMulticastGroup`, :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.leaveMulticastGroup`.
