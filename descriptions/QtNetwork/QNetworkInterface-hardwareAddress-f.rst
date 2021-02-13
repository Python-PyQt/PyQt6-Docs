.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: b72825ba9ccb8b1bba1e8fe945c34300

Returns the low-level hardware address for this interface. On Ethernet interfaces, this will be a MAC address in string representation, separated by colons.

Other interface types may have other types of hardware addresses. Implementations should not depend on this function returning a valid MAC address.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.type`.
