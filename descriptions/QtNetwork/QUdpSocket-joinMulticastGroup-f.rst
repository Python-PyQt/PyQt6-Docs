.. sip:method-description::
    :status: todo
    :pysig: 38da605de61b832a9dd48e47488be7fd
    :realsig: (const QHostAddress&)
    :digest: 6a9506a5c1f1d17f9f0c6081a9dc4778

Joins the multicast group specified by *groupAddress* on the default interface chosen by the operating system. The socket must be in BoundState, otherwise an error occurs.

Note that if you are attempting to join an IPv4 group, your socket must not be bound using IPv6 (or in dual mode, using :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.Any`). You must use :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.AnyIPv4` instead.

This function returns ``true`` if successful; otherwise it returns ``false`` and sets the socket error accordingly.

**Note:** Joining IPv6 multicast groups without an interface selection is not supported in all operating systems. Consider using the overload where the interface is specified.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.leaveMulticastGroup`.
