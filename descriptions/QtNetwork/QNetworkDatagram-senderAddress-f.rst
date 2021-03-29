.. sip:method-description::
    :status: todo
    :pysig: ec82a7f8c43ec9633e2975527eb9f362
    :realsig: () const
    :digest: 2b40661d8a755d2f1dc636f0d6fe131b

Returns the sender address associated with this datagram. For a datagram received from the network, it is the address of the peer node that sent the datagram. For an outgoing datagrams, it is the local address to be used when sending.

If no sender address was set on this datagram, the returned object will report true to :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isNull`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationAddress`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setSender`.
