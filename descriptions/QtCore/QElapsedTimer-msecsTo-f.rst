.. sip:method-description::
    :status: todo
    :pysig: ae37ca4aff0e0113e02871bc3305e3b3
    :realsig: (const QElapsedTimer&) const
    :digest: 4983ead3b09ea055580b0b1da4ac3da8

Returns the number of milliseconds between this :sip:ref:`~PyQt6.QtCore.QElapsedTimer` and *other*. If *other* was started before this object, the returned value will be negative. If it was started later, the returned value will be positive.

The return value is undefined if this object or *other* were invalidated.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.secsTo`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed`.
