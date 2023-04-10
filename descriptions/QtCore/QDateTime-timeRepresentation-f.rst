.. sip:method-description::
    :status: todo
    :pysig: 64057e5a182ab705ccb12c2b1f2a0b03
    :realsig: () const
    :digest: f9c0ab2494736e0bccb869f09f857411

Returns a :sip:ref:`~PyQt6.QtCore.QTimeZone` identifying how this datetime represents time.

The :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` of the returned :sip:ref:`~PyQt6.QtCore.QTimeZone` will coincide with that of this datetime; if it is not :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` then the returned :sip:ref:`~PyQt6.QtCore.QTimeZone` is a time representation. When their :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC`, the returned :sip:ref:`~PyQt6.QtCore.QTimeZone`'s fixedSecondsAheadOfUtc() supplies the offset. When :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone`, the :sip:ref:`~PyQt6.QtCore.QTimeZone` object itself is the full representation of that time zone.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.timeZone`, :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone`, :sip:ref:`~PyQt6.QtCore.QTimeZone.asBackendZone`.
