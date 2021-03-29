.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 8b11251a6abbd0b288a5df8256b73822

Returns the scope ID of an IPv6 address. For IPv4 addresses, or if the address does not contain a scope ID, an empty QString is returned.

The IPv6 scope ID specifies the scope of *reachability* for non-global IPv6 addresses, limiting the area in which the address can be used. All IPv6 addresses are associated with such a reachability scope. The scope ID is used to disambiguate addresses that are not guaranteed to be globally unique.

IPv6 specifies the following four levels of reachability:

* Node-local: Addresses that are only used for communicating with services on the same interface (e.g., the loopback interface "::1").

* Link-local: Addresses that are local to the network interface (\ *link*). There is always one link-local address for each IPv6 interface on your host. Link-local addresses ("fe80...") are generated from the MAC address of the local network adaptor, and are not guaranteed to be unique.

* Global: For globally routable addresses, such as public servers on the Internet.

When using a link-local or site-local address for IPv6 connections, you must specify the scope ID. The scope ID for a link-local address is usually the same as the interface name (e.g., "eth0", "en1") or number (e.g., "1", "2").

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.setScopeId`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.interfaceFromName`.
