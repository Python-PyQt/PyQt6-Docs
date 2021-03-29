.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 3465277c893ef3ad6b817e59960bed16

Returns the interface index this datagram is associated with. The interface index is a positive number that uniquely identifies the network interface in the operating system. This number matches the value returned by :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.index` for the interface.

If this datagram was received from the network, this is the index of the interface that the packet was received from. If this is an outgoing datagram, this is the index of the interface that the datagram should be sent on.

A value of 0 indicates that the interface index is unknown.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setInterfaceIndex`.
