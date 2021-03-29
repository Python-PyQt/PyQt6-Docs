.. sip:method-description::
    :status: todo
    :pysig: 38da605de61b832a9dd48e47488be7fd
    :realsig: (const QHostAddress&)
    :digest: 111967a5b99797183186e5c9edca922a

Leaves the multicast group specified by *groupAddress* on the default interface chosen by the operating system. The socket must be in :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.BoundState`, otherwise an error occurs.

This function returns ``true`` if successful; otherwise it returns ``false`` and sets the socket error accordingly.

**Note:** This function should be called with the same arguments as were passed to :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.joinMulticastGroup`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.joinMulticastGroup`.
