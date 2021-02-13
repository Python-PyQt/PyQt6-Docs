.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: ca1693c7c21a527a740594071d7ca1e9

Returns the data payload of this datagram. For a datagram received from the network, it contains the payload of the datagram. For an outgoing datagram, it is the datagram to be sent.

Note that datagrams can be transmitted with no data, so the returned :sip:ref:`~PyQt6.QtCore.QByteArray` may be empty.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.setData`.
