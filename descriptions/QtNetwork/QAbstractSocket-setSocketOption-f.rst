.. sip:method-description::
    :status: todo
    :pysig: b7474e6278473ccb4049c7c40501e563
    :realsig: (QAbstractSocket::SocketOption,const QVariant&)
    :digest: 4d8edfc0ae96a1cc2df744a1bbd65833

Sets the given *option* to the value described by *value*.

**Note:** Since the options are set on an internal socket the options only apply if the socket has been created. This is only guaranteed to have happened after a call to :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.bind`, or when :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connected` has been emitted.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.socketOption`.
