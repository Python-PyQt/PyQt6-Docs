.. sip:method-description::
    :status: todo
    :pysig: 64057e5a182ab705ccb12c2b1f2a0b03
    :realsig: () const
    :digest: 77e8e2b1b845474867b14715f2dc90fa

Returns the time zone of the datetime.

The result is the same as ``timeRepresentation().asBackendZone()``. In all cases, the result's :sip:ref:`~PyQt6.QtCore.QTimeZone.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone`.

When :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`, the result will describe local time at the time this method was called. It will not reflect subsequent changes to the system time zone, even when the :sip:ref:`~PyQt6.QtCore.QDateTime` from which it was obtained does.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.timeRepresentation`, :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone`, :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`, :sip:ref:`~PyQt6.QtCore.QTimeZone.asBackendZone`.
