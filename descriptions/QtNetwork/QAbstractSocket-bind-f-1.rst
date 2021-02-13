.. sip:method-description::
    :status: todo
    :pysig: fd3e11c2cbc38451263d560cf674ab60
    :realsig: (const QHostAddress&,quint16,QAbstractSocket::BindMode)
    :digest: d1eb13906744978fdc3e64b7a9f2e5dd

Binds to *address* on port *port*, using the BindMode *mode*.

For UDP sockets, after binding, the signal QUdpSocket::readyRead() is emitted whenever a UDP datagram arrives on the specified address and port. Thus, this function is useful to write UDP servers.

For TCP sockets, this function may be used to specify which interface to use for an outgoing connection, which is useful in case of multiple network interfaces.

By default, the socket is bound using the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.BindMode.DefaultForPlatform` BindMode. If a port is not specified, a random port is chosen.

On success, the function returns ``true`` and the socket enters :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.BoundState`; otherwise it returns ``false``.
