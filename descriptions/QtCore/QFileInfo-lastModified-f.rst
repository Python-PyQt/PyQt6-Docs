.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: 19198d84b102bb0341bf691c7f23e71e

Returns the date and local time when the file was last modified.

If the file is a symlink, the time of the target file is returned (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.birthTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`, :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileTime`.
