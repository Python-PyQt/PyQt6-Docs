.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 6877531b7422690e59a6df020f225215

Use :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone`\ (\ :sip:ref:`~PyQt6.QtCore.QTimeZone.fromSecondsAheadOfUtc`\ (offsetSeconds)) instead

Sets the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` and the offset to *offsetSeconds*. The datetime may refer to a different point in time.

The maximum and minimum offset is 14 positive or negative hours. If *offsetSeconds* is larger or smaller than that, then the result is undefined.

If *offsetSeconds* is 0 then the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` will be set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone`, :sip:ref:`~PyQt6.QtCore.QDateTime.isValid`, :sip:ref:`~PyQt6.QtCore.QDateTime.offsetFromUtc`, :sip:ref:`~PyQt6.QtCore.QDateTime.toOffsetFromUtc`.
