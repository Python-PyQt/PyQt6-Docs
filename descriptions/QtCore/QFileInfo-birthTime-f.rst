.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: 696547370b277889b64477927a43af6b

Returns the date and time when the file was created / born.

If the file birth time is not available, this function returns an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`.

If the file is a symlink, the time of the target file is returned (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`, :sip:ref:`~PyQt6.QtCore.QFileInfo.metadataChangeTime`.
