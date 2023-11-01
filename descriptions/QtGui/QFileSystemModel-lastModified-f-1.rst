.. sip:method-description::
    :status: todo
    :pysig: 4837500357b7dbf75f0f060a87daefc0
    :realsig: (const QModelIndex&, const QTimeZone&) const
    :digest: 7d446c1220077232b0b3af4d654448bb

Returns the date and time, in the time zone *tz*, when *index* was last modified.

Typical arguments for *tz* are ``QTimeZone::UTC`` or ``QTimeZone::LocalTime``. UTC does not require any conversion from the time returned by the native file system API, therefore getting the time in UTC is potentially faster. LocalTime is typically chosen if the time is shown to the user.

If *index* is invalid, a default constructed :sip:ref:`~PyQt6.QtCore.QDateTime` is returned.
