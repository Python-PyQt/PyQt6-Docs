.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: e63a9d6f6437f5dbb5388e74722a07d1

Returns the date and time when the file was created (born), in local time.

If the file birth time is not available, this function returns an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`.

If the file is a symlink, this function returns information about the target, not the symlink.

This function overloads QFileInfo::birthTime(const :sip:ref:`~PyQt6.QtCore.QTimeZone` &tz), and returns the same as ``birthTime(QTimeZone::LocalTime)``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`, :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`.
