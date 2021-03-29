.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 4e92b7b4667acc256d4f8ae9b7d59609

Returns the address as a string.

For example, if the address is the IPv4 address 127.0.0.1, the returned string is "127.0.0.1". For IPv6 the string format will follow the RFC5952 recommendation. For :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.Any`, its IPv4 address will be returned ("0.0.0.0")

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.toIPv4Address`.
