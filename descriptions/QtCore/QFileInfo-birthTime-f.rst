.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: 4060d740cd033d8896b384faa11ca80c

Returns the date and time when the file was created (born), in local time.

If the file birth time is not available, this function returns an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`.

If the file is a symlink, the time of the target file is returned (not the symlink).

This function overloads QFileInfo::birthTime(const :sip:ref:`~PyQt6.QtCore.QTimeZone` &tz), and returns the same as ``birthTime(QTimeZone::LocalTime)``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`, :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`.
