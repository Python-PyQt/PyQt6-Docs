.. sip:method-description::
    :status: todo
    :pysig: 211646a7dcb4c66055f9275ee3950565
    :realsig: () const
    :digest: 14f57b963820c4781e15c297912d2f64

Returns the deadline when this address becomes invalid and will be removed from the networking stack, if known. If the address lifetime is not known (see :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.isLifetimeKnown`), this function always returns :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.ForeverConstant.Forever`.

While an address is valid, it will be accepted by the operating system as a valid destination address for this machine. Whether it is used as a source address for new, outgoing packets is controlled by, among other rules, the preferred lifetime (see :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.preferredLifetime`).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.preferredLifetime`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.isLifetimeKnown`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.setAddressLifetime`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAddressEntry.clearAddressLifetime`.
