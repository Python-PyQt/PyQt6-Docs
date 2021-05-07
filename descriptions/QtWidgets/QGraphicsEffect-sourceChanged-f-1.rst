.. sip:method-description::
    :status: todo
    :pysig: 7272e70d1c95058321114923906ef9e5
    :realsig: (QGraphicsEffect::ChangeFlags)
    :digest: fcbdf08519d5e2b0669e9fd269d4440a

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect` to notify the effect that the source has changed. If the effect applies any cache, then this cache must be purged in order to reflect the new appearance of the source.

The *flags* describes what has changed.
