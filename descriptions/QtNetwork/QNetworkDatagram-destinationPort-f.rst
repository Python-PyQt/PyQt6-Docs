.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: d7b58196201862cb83f04036fc9d11d2

Returns the port number of the destination associated with this datagram. For a datagram received from the network, it is the local port number that the peer node sent the datagram to. For an outgoing datagram, it is the peer port the datagram should be sent to.

If no destination address was associated with this datagram, this function returns -1.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationAddress`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setDestination`.
