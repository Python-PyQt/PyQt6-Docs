.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: 0ed6a6da355033933a4996498babe63b

Returns the date and local time when the file was last read (accessed).

On platforms where this information is not available, returns the same as :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`.

If the file is a symlink, the time of the target file is returned (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`.
