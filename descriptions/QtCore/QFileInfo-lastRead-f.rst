.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: 7e7dc582fc2bdc560bb688110d23b012

Returns the date and time when the file was last read (accessed).

On platforms where this information is not available, returns the same time as :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`.

If the file is a symlink, this function returns information about the target, not the symlink.

This function overloads QFileInfo::lastRead(const QTimeZone &), and returns the same as ``lastRead(QTimeZone::LocalTime)``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`.
