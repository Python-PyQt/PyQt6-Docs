.. sip:method-description::
    :status: todo
    :pysig: 38da605de61b832a9dd48e47488be7fd
    :realsig: (const QHostAddress&)
    :digest: a84d5ec02a0b143a4a283e77cac4951e

Joins the multicast group specified by *groupAddress* on the default interface chosen by the operating system. The socket must be in :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.BoundState`, otherwise an error occurs.

Note that if you are attempting to join an IPv4 group, your socket must not be bound using IPv6 (or in dual mode, using :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.Any`). You must use :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.AnyIPv4` instead.

This function returns ``true`` if successful; otherwise it returns ``false`` and sets the socket error accordingly.

**Note:** Joining IPv6 multicast groups without an interface selection is not supported in all operating systems. Consider using the overload where the interface is specified.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.leaveMulticastGroup`.
