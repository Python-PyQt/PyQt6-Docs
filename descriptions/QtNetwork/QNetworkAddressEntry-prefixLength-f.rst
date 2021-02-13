.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 39f603dcfdee4b71dcee3434bc0cb439

Returns the prefix length of this IP address. The prefix length matches the number of bits set to 1 in the netmask (see :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.netmask`). For IPv4 addresses, the value is between 0 and 32. For IPv6 addresses, it's contained between 0 and 128 and is the preferred form of representing addresses.

This function returns -1 if the prefix length could not be determined (i.e., :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.netmask` returns a null QHostAddress()).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.setPrefixLength`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.netmask`.
