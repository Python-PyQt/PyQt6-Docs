.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 9207c4eaf5769ee3118fe5f362eb939a

Returns the port number of the sender associated with this datagram. For a datagram received from the network, it is the port number that the peer node sent the datagram from. For an outgoing datagram, it is the local port the datagram should be sent from.

If no sender address was associated with this datagram, this function returns -1.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderAddress`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setSender`.
