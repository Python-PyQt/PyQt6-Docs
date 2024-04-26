.. sip:method-description::
    :status: todo
    :pysig: dc0ffe100c10dc1b7bf734884dd630c6
    :realsig: (QFileDevice::FileTime) const
    :digest: c56e8346868305e1b379eb8176befd3d

Returns the file time specified by *time*.

If the time cannot be determined, an invalid date time is returned.

If the file is a symlink, this function returns information about the target, not the symlink.

This function overloads QFileInfo::fileTime(QFileDevice::FileTime, const QTimeZone &), and returns the same as ``fileTime(time, QTimeZone::LocalTime)``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`, :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`.
