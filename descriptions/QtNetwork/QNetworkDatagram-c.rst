.. sip:class-description::
    :status: todo
    :brief: The data and metadata of a UDP datagram
    :digest: 654fe09edc301fdae45cb332e2cd60aa

The :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram` class provides the data and metadata of a UDP datagram.

:sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram` can be used with the :sip:ref:`~PyQt6.QtNetwork.QUdpSocket` class to represent the full information contained in a UDP (User Datagram Protocol) datagram. :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram` encapsulates the following information of a datagram:

* the payload data;

* the sender address and port number;

* the destination address and port number;

* the remaining hop count limit (on IPv4, this field is usually called "time to live" - TTL);

* the network interface index the datagram was received on or to be sent on.

:sip:ref:`~PyQt6.QtNetwork.QUdpSocket` will try to match a common behavior as much as possible on all operating systems, but not all of the metadata above can be obtained in some operating systems. Metadata that cannot be set on the datagram when sending with :sip:ref:`~PyQt6.QtNetwork.QUdpSocket.writeDatagram` will be silently discarded.

Upon reception, the :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderAddress` and :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderPort` properties contain the address and port of the peer that sent the datagram, while :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationAddress` and :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationPort` contain the target that was contained in the datagram. That is usually an address local to the current machine, but it can also be an IPv4 broadcast address (such as "255.255.255.255") or an IPv4 or IPv6 multicast address. Applications may find it useful to determine if the datagram was sent specifically to this machine via unicast addressing or whether it was sent to multiple destinations.

When sending, the :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderAddress` and :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderPort` should contain the local address to be used when sending. The sender address must be an address that is assigned to this machine, which can be obtained using :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`, and the port number must be the port number that the socket is bound to. Either field can be left unset and will be filled in by the operating system with default values. The :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationAddress` and :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationPort` fields may be set to a target address different from the one the UDP socket is currently associated with.

Usually, when sending a datagram in reply to a datagram previously received, one will set the :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.destinationAddress` to be the :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.senderAddress` of the incoming datagram and similarly for the port numbers. To facilitate this common process, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram` provides the function :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.makeReply`.

The hopCount() function contains, for a received datagram, the remaining hop count limit for the packet. When sending, it contains the hop count limit to be set. Most protocols will leave this value set to the default and let the operating system decide on the best value to be used. Multicasting over IPv4 often uses this field to indicate the scope of the multicast group (link-local, local to an organization or global).

The :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.interfaceIndex` function contains the index of the operating system's interface that received the packet. This value is the same one that can be set on a :sip:ref:`~PyQt6.QtNetwork.QHostAddress.scopeId` property and matches the :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.index` property. When sending packets to global addresses, it is not necessary to set the interface index as the operating system will choose the correct one using the system routing table. This property is important when sending datagrams to link-local destinations, whether unicast or multicast.

.. _qnetworkdatagram-feature-support:

Feature support
---------------

Some features of :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram` are not supported in all operating systems. Only the address and ports of the remote host (sender in received packets and destination for outgoing packets) are supported in all systems. On most operating systems, the other features are supported only for IPv6. Software should check at runtime whether the rest could be determined for IPv4 addresses.

The current feature support is as follows:

+--------------------------------+---------------+---------------+-----------------+
| Operating system               | Local address | Hop count     | Interface index |
+================================+===============+===============+=================+
| FreeBSD                        | Supported     | Supported     | Only for IPv6   |
+--------------------------------+---------------+---------------+-----------------+
| Linux                          | Supported     | Supported     | Supported       |
+--------------------------------+---------------+---------------+-----------------+
| OS X                           | Supported     | Supported     | Only for IPv6   |
+--------------------------------+---------------+---------------+-----------------+
| Other Unix supporting RFC 3542 | Only for IPv6 | Only for IPv6 | Only for IPv6   |
+--------------------------------+---------------+---------------+-----------------+
| Windows (desktop)              | Supported     | Supported     | Supported       |
+--------------------------------+---------------+---------------+-----------------+
| Windows RT                     | Not supported | Not supported | Not supported   |
+--------------------------------+---------------+---------------+-----------------+

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`.
