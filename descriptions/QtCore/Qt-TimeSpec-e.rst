.. sip:enum-description::
    :status: todo
    :digest: b2c3b70c2a3645e00a8ad06a369a8443

Both LocalTime and TimeZone will take care of transitions, such as the start and end of daylight-saving time. UTC is the standard time relative to which time-zones are usually specified: Greenwich Mean Time has zero offset from it. Neither UTC nor OffsetFromUTC has any transitions.

When specifying a datetime using OffsetFromUTC, the offset from UTC must also be supplied (it is measured in seconds). To specify a datetime using TimeZone, a :sip:ref:`~PyQt6.QtCore.QTimeZone` must be supplied. From Qt 6.5, a :sip:ref:`~PyQt6.QtCore.QTimeZone` can now package a timespec with, where needed, an offset as a lightweight time description, so that passing a :sip:ref:`~PyQt6.QtCore.QTimeZone` now provides a uniform way to use datetime APIs, saving the need to call them differently for different timespecs.

**Note:** After a change to the system time-zone setting, the behavior of LocalTime-based :sip:ref:`~PyQt6.QtCore.QDateTime` objects created before the change is undefined: :sip:ref:`~PyQt6.QtCore.QDateTime` may have cached data that the change invalidates. (This is not triggered by *transitions* of the system time-zone.) In long-running processes, updates to the system's time-zone data (e.g. when politicians change the rules for a zone) may likewise lead to conflicts between the updated time-zone information and data cached by :sip:ref:`~PyQt6.QtCore.QDateTime` objects created before the update, using either LocalTime or TimeZone.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone`, :sip:ref:`~PyQt6.QtCore.QDateTime`.
