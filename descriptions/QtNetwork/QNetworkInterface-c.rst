.. sip:class-description::
    :status: todo
    :brief: Listing of the host's IP addresses and network interfaces
    :digest: 3f41d4be0692c79400f51ee6632a5fcc

The :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface` class provides a listing of the host's IP addresses and network interfaces.

:sip:ref:`~PyQt6.QtNetwork.QNetworkInterface` represents one network interface attached to the host where the program is being run. Each network interface may contain zero or more IP addresses, each of which is optionally associated with a netmask and/or a broadcast address. The list of such trios can be obtained with :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.addressEntries`. Alternatively, when the netmask or the broadcast addresses or other information aren't necessary, use the :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.allAddresses` convenience function to obtain just the IP addresses of the active interfaces.

:sip:ref:`~PyQt6.QtNetwork.QNetworkInterface` also reports the interface's hardware address with :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.hardwareAddress`.

Not all operating systems support reporting all features. Only the IPv4 addresses are guaranteed to be listed by this class in all platforms. In particular, IPv6 address listing is only supported on Windows, Linux, macOS and the BSDs.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry`.
