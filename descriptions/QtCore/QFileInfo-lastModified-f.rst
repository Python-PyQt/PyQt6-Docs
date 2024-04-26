.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: 0fdd9f8eb32c28943f4c3d2fb0d64434

Returns the date and time when the file was last modified.

If the file is a symlink, this function returns information about the target, not the symlink.

This function overloads QFileInfo::lastModified(const QTimeZone &), and returns the same as ``lastModified(QTimeZone::LocalTime)``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`, :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`.
