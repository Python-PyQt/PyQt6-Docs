.. sip:method-description::
    :status: todo
    :pysig: e105a5380d1337eb62c301ebb55a367a
    :realsig: (QFileDevice::FileTime, const QTimeZone&) const
    :digest: c0f09ee42781c2cbc5bd4de85df8b603

Returns the file time specified by *time*.

The returned time is in the time zone specified by *tz*. For example, you can use :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.LocalTime` or :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` to get the time in the Local time zone or UTC, respectively. Since native file system API typically uses UTC, using :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` is often faster, as it does not require any conversions.

If the time cannot be determined, an invalid date time is returned.

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: birthTime(const QTimeZone &), lastModified(const QTimeZone &), lastRead(const QTimeZone &), metadataChangeTime(const QTimeZone &), :sip:ref:`~PyQt6.QtCore.QDateTime.isValid`.
