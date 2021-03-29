.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&) const
    :digest: e10f29808133b50d2d5ae739f5d8c7b0

Returns ``true`` if the file called *name* exists; otherwise returns false.

Unless *name* contains an absolute file path, the file name is assumed to be relative to the directory itself, so this function is typically used to check for the presence of files within a directory.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.exists`, :sip:ref:`~PyQt6.QtCore.QFile.exists`.
