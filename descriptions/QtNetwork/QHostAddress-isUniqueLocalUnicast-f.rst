.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ac7cd1a4c01b91970c12197e19f5998a

Returns ``true`` if the address is an IPv6 unique local unicast address, ``false`` otherwise.

An IPv6 unique local unicast address is one in the network fc00::/7. See the `IANA IPv6 Address Space <https://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml>`_ registry for more information.

Note that Unique local unicast addresses count as global addresses too. RFC 4193 says that, in practice, "applications may treat these addresses like global scoped addresses." Only routers need care about the distinction.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isLoopback`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isGlobal`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isMulticast`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isLinkLocal`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isPrivateUse`.
