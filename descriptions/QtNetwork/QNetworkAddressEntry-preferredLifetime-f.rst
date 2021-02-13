.. sip:method-description::
    :status: todo
    :pysig: 211646a7dcb4c66055f9275ee3950565
    :realsig: () const
    :digest: 3cbec5c35ef8eb6685c571c5585d1110

Returns the deadline when this address becomes deprecated (no longer preferred), if known. If the address lifetime is not known (see :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.isLifetimeKnown`), this function always returns :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.ForeverConstant.Forever`.

While an address is preferred, it may be used by the operating system as the source address for new, outgoing packets. After it becomes deprecated, it will remain valid for incoming packets for a while longer until finally removed (see :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.validityLifetime`).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.validityLifetime`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.isLifetimeKnown`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.setAddressLifetime`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.clearAddressLifetime`.
