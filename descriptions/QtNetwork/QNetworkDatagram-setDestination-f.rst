.. sip:method-description::
    :status: todo
    :pysig: a9bb3cdd730e6b72fdc0b732361dcf79
    :realsig: (const QHostAddress&,quint16)
    :digest: 506f278abc7b1d054ced115c07daffec

Sets the destination address associated with this datagram to be the address *address* and port number *port*. The destination address and port numbers are usually set by :sip:ref:`~PyQt6.QtNetwork.QUdpSocket` upon reception, so there's no need to call this function on a received datagram.

For outgoing datagrams, this function can be used to set the address the datagram should be sent to. It can be the unicast address used to communicate with the peer or a broadcast or multicast address to send to a group of devices.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.writeDatagram`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationAddress`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setSender`.
