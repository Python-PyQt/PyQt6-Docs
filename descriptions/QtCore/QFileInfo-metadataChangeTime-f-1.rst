.. sip:method-description::
    :status: todo
    :pysig: 25c78415fd7487087c7fbba8b11ae943
    :realsig: (const QTimeZone&) const
    :digest: 70f0ebab19f33c6b394db2039c8c4fbc

Returns the date and time when the file's metadata was last changed. A metadata change occurs when the file is first created, but it also occurs whenever the user writes or sets inode information (for example, changing the file permissions).

The returned time is in the time zone specified by *tz*. For example, you can use :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.LocalTime` or :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` to get the time in the Local time zone or UTC, respectively. Since native file system API typically uses UTC, using :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` is often faster, as it does not require any conversions.

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: birthTime(const QTimeZone &), lastModified(const QTimeZone &), lastRead(const QTimeZone &), fileTime(QFileDevice::FileTime time, const QTimeZone &).
