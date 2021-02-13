.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 66bd233bba72ce8039df4d14b12a9ef9

Returns the maximum transmission unit on this interface, if known, or 0 otherwise.

The maximum transmission unit is the largest packet that may be sent on this interface without incurring link-level fragmentation. Applications may use this value to calculate the size of the payload that will fit an unfragmented UDP datagram. Remember to subtract the sizes of headers used in your communication over the interface, e.g. TCP (20 bytes) or UDP (12), IPv4 (20) or IPv6 (40, absent some form of header compression), when computing how big a payload you can transmit. Also note that the MTU along the full path (the Path MTU) to the destination may be smaller than the interface's MTU.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`.
