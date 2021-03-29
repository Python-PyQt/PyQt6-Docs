.. sip:method-description::
    :status: todo
    :pysig: ec82a7f8c43ec9633e2975527eb9f362
    :realsig: () const
    :digest: 28593fa4eb122d56f52d6cdc32b50559

Returns the destination address associated with this datagram. For a datagram received from the network, it is the address the peer node sent the datagram to, which can either be a local address of this machine or a multicast or broadcast address. For an outgoing datagrams, it is the address the datagram should be sent to.

If no destination address was set on this datagram, the returned object will report true to :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isNull`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderAddress`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setDestination`.
