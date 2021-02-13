.. sip:method-description::
    :status: todo
    :pysig: 4ce207d4f9a288378bd94fa50174e2b1
    :realsig: (const QHostAddress&,quint16)
    :digest: 380c6865ac334d2762617ebc7b700119

Sets the sender address associated with this datagram to be the address *address* and port number *port*. The sender address and port numbers are usually set by :sip:ref:`~PyQt6.QtNetwork.QUdpSocket` upon reception, so there's no need to call this function on a received datagram.

For outgoing datagrams, this function can be used to set the address the datagram should carry. The address *address* must usually be one of the local addresses assigned to this machine, which can be obtained using :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`. If left unset, the operating system will choose the most appropriate address to use given the destination in question.

The port number *port* must be the port number associated with the socket, if there is one. The value of 0 can be used to indicate that the operating system should choose the port number.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.writeDatagram`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderAddress`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setDestination`.
