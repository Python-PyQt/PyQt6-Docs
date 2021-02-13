.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 3620b98d3861d283a6d6fc480f4fedec

Returns ``true`` if the address is the IPv4 broadcast address, ``false`` otherwise. The IPv4 broadcast address is 255.255.255.255.

Note that this function does not return true for an IPv4 network's local broadcast address. For that, please use :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface` to obtain the broadcast addresses of the local machine.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isLoopback`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isGlobal`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isMulticast`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isLinkLocal`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isUniqueLocalUnicast`.
