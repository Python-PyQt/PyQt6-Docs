.. sip:method-description::
    :status: todo
    :pysig: 25c78415fd7487087c7fbba8b11ae943
    :realsig: (const QTimeZone&) const
    :digest: 8c871fe6036d29a79368a3ea081166c1

Returns the date and time when the file was last modified.

The returned time is in the time zone specified by *tz*. For example, you can use :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.LocalTime` or :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` to get the time in the Local time zone or UTC, respectively. Since native file system API typically uses UTC, using :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` is often faster, as it does not require any conversions.

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: birthTime(const QTimeZone &), lastRead(const QTimeZone &), metadataChangeTime(const QTimeZone &), fileTime(QFileDevice::FileTime, const QTimeZone &).
