.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: d36cfefb2d1562f8e610aba8519f5dd7

Returns ``true`` if the address is an IPv6 site-local address, ``false`` otherwise.

An IPv6 site-local address is one in the network fec0::/10. See the `IANA IPv6 Address Space <https://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml>`_ registry for more information.

IPv6 site-local addresses are deprecated and should not be depended upon in new applications. New applications should not depend on this function and should consider site-local addresses the same as global (which is why :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isGlobal` also returns true). Site-local addresses were replaced by Unique Local Addresses (ULA).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isLoopback`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isGlobal`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isMulticast`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isLinkLocal`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isUniqueLocalUnicast`.
