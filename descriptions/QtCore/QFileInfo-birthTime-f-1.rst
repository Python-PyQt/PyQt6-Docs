.. sip:method-description::
    :status: todo
    :pysig: 25c78415fd7487087c7fbba8b11ae943
    :realsig: (const QTimeZone&) const
    :digest: 3adc88d3d168d40fd253142469154e55

Returns the date and time when the file was created (born).

The returned time is in the time zone specified by *tz*. For example, you can use :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.LocalTime` or :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` to get the time in the Local time zone or UTC, respectively. Since native file system API typically uses UTC, using :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.UTC` is often faster, as it does not require any conversions.

If the file birth time is not available, this function returns an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`.

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: lastModified(const QTimeZone &), lastRead(const QTimeZone &), metadataChangeTime(const QTimeZone &), fileTime(QFileDevice::FileTime, const QTimeZone &).
