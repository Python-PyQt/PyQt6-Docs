.. sip:method-description::
    :status: todo
    :pysig: 817aa0f35270d1546897de7c4de37187
    :realsig: (const QString&)
    :digest: d9f4239187f26df74b6abd6b12e69e4f

Parses the IP and subnet information contained in *subnet* and returns the network prefix for that network and its prefix length.

The IP address and the netmask must be separated by a slash (/).

This function supports arguments in the form:

* 123.123.123.123/n where n is any value between 0 and 32

* 123.123.123.123/255.255.255.255

* <ipv6-address>/n where n is any value between 0 and 128

For IP version 4, this function accepts as well missing trailing components (i.e., less than 4 octets, like "192.168.1"), followed or not by a dot. If the netmask is also missing in that case, it is set to the number of octets actually passed (in the example above, it would be 24, for 3 octets).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.isInSubnet`.
