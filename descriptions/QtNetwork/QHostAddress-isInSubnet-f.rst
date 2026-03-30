.. sip:method-description::
    :status: todo
    :pysig: 22ecdab1e8df34d1569765abd8fd3a73
    :realsig: (const std::pair<QHostAddress, int>&) const
    :digest: f5b08de1485980f70a5ecff4262509a0

Returns ``true`` if this IP is in the subnet described by *subnet*. The :sip:ref:`~PyQt6.QtNetwork.QHostAddress` member of *subnet* contains the network prefix and the int (second) member contains the netmask (prefix length).
