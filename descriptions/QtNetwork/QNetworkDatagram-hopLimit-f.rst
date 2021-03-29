.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 32cb81643ffe62c830e3834fa55d797f

Returns the hop count limit associated with this datagram. The hop count limit is the number of nodes that are allowed to forward the IP packet before it expires and an error is sent back to the sender of the datagram. In IPv4, this value is usually known as "time to live" (TTL).

If this datagram was received from the network, this is the remaining hop count of the datagram after reception and was decremented by 1 by each node that forwarded the packet. A value of -1 indicates that the hop limit count not be obtained.

If this is an outgoing datagram, this is the value to be set in the IP header upon sending. A value of -1 indicates the operating system should choose the value.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setHopLimit`.
