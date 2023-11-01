.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: 9bde7d7f81c13aa5410c65fffa8a5b89

Returns the date and time when the file was last read (accessed).

On platforms where this information is not available, returns the same time as :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`.

If the file is a symlink, the time of the target file is returned (not the symlink).

This function overloads QFileInfo::lastRead(const QTimeZone &), and returns the same as ``lastRead(QTimeZone::LocalTime)``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`.
