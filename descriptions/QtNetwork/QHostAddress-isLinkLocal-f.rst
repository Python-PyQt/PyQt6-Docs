.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 022ac14ccbba31cf82bd82a4b526b947

Returns ``true`` if the address is an IPv4 or IPv6 link-local address, ``false`` otherwise.

An IPv4 link-local address is an address in the network 169.254.0.0/16. An IPv6 link-local address is one in the network fe80::/10. See the `IANA IPv6 Address Space <https://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml>`_ registry for more information.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isLoopback`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isGlobal`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isMulticast`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isSiteLocal`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isUniqueLocalUnicast`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isPrivateUse`.
