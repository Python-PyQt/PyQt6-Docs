.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: 42a15149df444522e06fdbbf401e4e24

Returns the date and time when the file's metadata was last changed, in local time.

A metadata change occurs when the file is first created, but it also occurs whenever the user writes or sets inode information (for example, changing the file permissions).

If the file is a symlink, the time of the target file is returned (not the symlink).

This function overloads QFileInfo::metadataChangeTime(const :sip:ref:`~PyQt6.QtCore.QTimeZone` &tz), and returns the same as ``metadataChangeTime(QTimeZone::LocalTime)``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`.
