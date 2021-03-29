.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (bool*) const
    :digest: af79226b9cddddf8dc2b8e338b39c6a7

Returns the IPv4 address as a number.

For example, if the address is 127.0.0.1, the returned value is 2130706433 (i.e. 0x7f000001).

This value is valid if the :sip:ref:`~PyQt6.QtNetwork.QHostAddress.protocol` is :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.IPv4Protocol`, or if the protocol is :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.IPv6Protocol`, and the IPv6 address is an IPv4 mapped address (RFC4291). In those cases, *ok* will be set to true. Otherwise, it will be set to false.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.toString`.
