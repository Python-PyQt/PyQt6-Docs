.. sip:method-description::
    :status: todo
    :pysig: ffb5c77f6be2ae0d97654825b3b60e67
    :realsig: (int) const
    :digest: 01ae7fee32b25027b48af0e5d683c196

Returns a :sip:ref:`~PyQt6.QtCore.QTime` object containing a time *ms* milliseconds later than the time of this object (or earlier if *ms* is negative).

Note that the time will wrap if it passes midnight. See :sip:ref:`~PyQt6.QtCore.QTime.addSecs` for an example.

Returns a null time if this time is invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime.addSecs`, :sip:ref:`~PyQt6.QtCore.QTime.msecsTo`, :sip:ref:`~PyQt6.QtCore.QDateTime.addMSecs`.
