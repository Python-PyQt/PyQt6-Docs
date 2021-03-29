.. sip:method-description::
    :status: todo
    :pysig: b380d089c1079402e74d8dd92b401444
    :realsig: (const QHostAddress&,int) const
    :digest: d33f52270dab098b7dc1187e3340a1b2

Returns ``true`` if this IP is in the subnet described by the network prefix *subnet* and netmask *netmask*.

An IP is considered to belong to a subnet if it is contained between the lowest and the highest address in that subnet. In the case of IP version 4, the lowest address is the network address, while the highest address is the broadcast address.

The *subnet* argument does not have to be the actual network address (the lowest address in the subnet). It can be any valid IP belonging to that subnet. In particular, if it is equal to the IP address held by this object, this function will always return true (provided the netmask is a valid value).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.parseSubnet`.
