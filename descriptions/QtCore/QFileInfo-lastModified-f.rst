.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: 019d31aa4f0d0843cd4e2228e9ec9f37

Returns the date and time when the file was last modified.

If the file is a symlink, the time of the target file is returned (not the symlink).

This function overloads QFileInfo::lastModified(const QTimeZone &), and returns the same as ``lastModified(QTimeZone::LocalTime)``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`, :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`.
