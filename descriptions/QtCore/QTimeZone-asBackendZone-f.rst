.. sip:method-description::
    :status: todo
    :pysig: 64057e5a182ab705ccb12c2b1f2a0b03
    :realsig: () const
    :digest: 69728277a09214bc80ab8f39d309dbdf

Converts this :sip:ref:`~PyQt6.QtCore.QTimeZone` to one whose :sip:ref:`~PyQt6.QtCore.QTimeZone.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone`.

In all cases, the result's :sip:ref:`~PyQt6.QtCore.QTimeZone.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone`. When this :sip:ref:`~PyQt6.QtCore.QTimeZone`'s :sip:ref:`~PyQt6.QtCore.QTimeZone.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone`, this :sip:ref:`~PyQt6.QtCore.QTimeZone` itself is returned.

If :sip:ref:`~PyQt6.QtCore.QTimeZone.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`, :sip:ref:`~PyQt6.QtCore.QTimeZone.utc` is returned. If it is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` then :sip:ref:`~PyQt6.QtCore.QTimeZone`\ (int) is passed its offset and the result is returned.

If :sip:ref:`~PyQt6.QtCore.QTimeZone.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` then an instance of the current system time zone will be returned. This will not change to reflect any subsequent change to the system time zone. It represents the local time that was in effect when asBackendZone() was called.

When using a lightweight time representation - local time, UTC time or time at a fixed offset from UTC - using methods only supported when feature ``timezone`` is enabled may be more expensive than using a corresponding time zone. This method maps a lightweight time representation to a corresponding time zone - that is, an instance based on system-supplied or standard data.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: QTimeZone(QTimeZone::Initialization), :sip:ref:`~PyQt6.QtCore.QTimeZone.fromSecondsAheadOfUtc`.
