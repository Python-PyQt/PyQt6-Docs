.. sip:method-description::
    :status: todo
    :pysig: 983858b4ac8cbe044dcbbb5646f34317
    :realsig: (const QString&)
    :digest: 78e0c6d6389e020262d2b70bb2724c9e

Returns a :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface` object for the interface named *name*. If no such interface exists, this function returns an invalid :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface` object.

The string *name* may be either an actual interface name (such as "eth0" or "en1") or an interface index in string form ("1", "2", etc.).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.name`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.isValid`.
