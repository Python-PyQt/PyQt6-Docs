.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: b5be27df3d359a2a54f9cfcd74fc104f

Try to optimize the socket for low latency. For a :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` this would set the TCP_NODELAY option and disable Nagle's algorithm. Set this to 1 to enable.
