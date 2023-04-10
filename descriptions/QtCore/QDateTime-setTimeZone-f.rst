.. sip:method-description::
    :status: todo
    :pysig: 64057e5a182ab705ccb12c2b1f2a0b03
    :realsig: (const QTimeZone&)
    :digest: 934ee80163ec368f3a8d840820908f2a

Sets the time zone used in this datetime to *toZone*.

The datetime may refer to a different point in time. It uses the time representation of *toZone*, which may change the meaning of its unchanged :sip:ref:`~PyQt6.QtCore.QDateTime.date` and :sip:ref:`~PyQt6.QtCore.QDateTime.time`.

If *toZone* is invalid then the datetime will be invalid. Otherwise, this datetime's :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` after the call will match ``toZone.timeSpec()``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.timeRepresentation`, :sip:ref:`~PyQt6.QtCore.QDateTime.timeZone`, :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`.
