.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: afc76cd1df1677e0f1a32d96d41bbcd9

Sets the prefix length of this IP address to *length*. The value of *length* must be valid for this type of IP address: between 0 and 32 for IPv4 addresses, between 0 and 128 for IPv6 addresses. Setting to any invalid value is equivalent to setting to -1, which means "no prefix length".

Setting the prefix length also sets the netmask (see :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.netmask`).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.prefixLength`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.setNetmask`.
