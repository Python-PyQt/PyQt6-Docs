.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: a1860210e83c84f6d5eeb18172a6260e

Sets the hop count limit associated with this datagram to *count*. The hop count limit is the number of nodes that are allowed to forward the IP packet before it expires and an error is sent back to the sender of the datagram. In IPv4, this value is usually known as "time to live" (TTL).

It is usually not necessary to call this function on datagrams received from the network.

If this is an outgoing packet, this is the value to be set in the IP header upon sending. The valid range for the value is 1 to 255. This function also accepts a value of -1 to indicate that the operating system should choose the value.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.hopLimit`.
