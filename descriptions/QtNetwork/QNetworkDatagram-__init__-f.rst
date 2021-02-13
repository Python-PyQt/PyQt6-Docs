.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 4b4326b3497cac5eb77d15ff53b5241e

Creates a :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram` object with no payload data and undefined destination address.

The payload can be modified by using :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setData` and the destination address can be set with :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setDestination`.

If the destination address is left undefined, :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.writeDatagram` will attempt to send the datagram to the address last associated with, by using QUdpSocket::connectToHost().
