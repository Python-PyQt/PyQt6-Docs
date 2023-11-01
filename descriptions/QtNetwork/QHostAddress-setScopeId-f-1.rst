.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 2ad149c86b3d13e38ea7ddb1a5a2fd16

Sets the IPv6 scope ID of the address to *id*. If the address protocol is not IPv6, this function does nothing. The scope ID may be set as an interface name (such as "eth0" or "en1") or as an integer representing the interface index. If *id* is an interface name, :sip:ref:`~PyQt6.QtNetwork` will convert to an interface index using :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.interfaceIndexFromName` before calling the operating system networking functions.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.scopeId`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.interfaceFromName`.
