.. sip:method-description::
    :status: todo
    :pysig: 140f232b1721aa5a9de2aef8ee6b5cb5
    :realsig: (QNearFieldTarget::AccessMethod) const
    :digest: 25e5e06379993079bdff6f1d0ba861fe

Returns ``true`` if the underlying device has a NFC adapter; otherwise returns ``false``. If an *accessMethod* is given, the function returns ``true`` only if the NFC adapter supports the given *accessMethod*.

.. seealso:: :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.isEnabled`.
