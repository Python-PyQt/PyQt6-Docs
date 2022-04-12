.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 9bc5698bfc5008d71d3022d43d898ddc

Returns ``true`` if the address is an IPv4 or IPv6 global address, ``false`` otherwise. A global address is an address that is not reserved for special purposes (like loopback or multicast) or future purposes.

Note that IPv6 unique local unicast addresses are considered global addresses (see :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isUniqueLocalUnicast`), as are IPv4 addresses reserved for local networks by RFC 1918.

Also note that IPv6 site-local addresses are deprecated and should be considered as global in new applications. This function returns true for site-local addresses too.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isLoopback`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isSiteLocal`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isUniqueLocalUnicast`.
