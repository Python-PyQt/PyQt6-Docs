.. sip:method-description::
    :status: todo
    :pysig: ec82a7f8c43ec9633e2975527eb9f362
    :realsig: () const
    :digest: a1e0f7e393c3793a23acf5530de60ca5

Returns the netmask associated with the IP address. The netmask is expressed in the form of an IP address, such as 255.255.0.0.

For IPv6 addresses, the prefix length is converted to an address where the number of bits set to 1 is equal to the prefix length. For a prefix length of 64 bits (the most common value), the netmask will be expressed as a :sip:ref:`~PyQt6.QtNetwork.QHostAddress` holding the address FFFF:FFFF:FFFF:FFFF::

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.setNetmask`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.prefixLength`.
