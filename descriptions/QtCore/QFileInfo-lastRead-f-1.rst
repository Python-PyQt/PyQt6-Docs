.. sip:method-description::
    :status: todo
    :pysig: 25c78415fd7487087c7fbba8b11ae943
    :realsig: (const QTimeZone&) const
    :digest: 9e1c33a6e86e3251dc1acbc67dc668a2

Returns the date and time when the file was last read (accessed).

The returned time is in the time zone specified by *tz*. For example, you can use :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.LocalTime` or :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` to get the time in the Local time zone or UTC, respectively. Since native file system API typically uses UTC, using :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` is often faster, as it does not require any conversions.

On platforms where this information is not available, returns the same time as :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`.

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: birthTime(const QTimeZone &), lastModified(const QTimeZone &), metadataChangeTime(const QTimeZone &), fileTime(QFileDevice::FileTime, const QTimeZone &).
