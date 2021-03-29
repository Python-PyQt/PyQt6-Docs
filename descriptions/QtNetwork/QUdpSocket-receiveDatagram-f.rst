.. sip:method-description::
    :status: todo
    :pysig: e8128a2ebd7a2e90b18a64d9d536ae7d
    :realsig: (qint64)
    :digest: 984df54e1811e59111fe4d0111024ad8

Receives a datagram no larger than *maxSize* bytes and returns it in the :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram` object, along with the sender's host address and port. If possible, this function will also try to determine the datagram's destination address, port, and the number of hop counts at reception time.

On failure, returns a :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram` that reports :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.isValid`.

If *maxSize* is too small, the rest of the datagram will be lost. If *maxSize* is 0, the datagram will be discarded. If *maxSize* is -1 (the default), this function will attempt to read the entire datagram.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.writeDatagram`, :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.hasPendingDatagrams`, :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.pendingDatagramSize`.
