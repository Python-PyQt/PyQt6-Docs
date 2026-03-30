.. sip:method-description::
    :status: todo
    :pysig: 502f7d3e77c89e5ef63bfbd42eaccbfd
    :realsig: (const QString&)
    :digest: 0f482a3db9a5c2d49ff1e111098dce52

This is the same as :sip:ref:`~PyQt6.QtCore.QTemporaryFile.rename`, except that it atomically replaces *newName* if it already exists, like :sip:ref:`~PyQt6.QtCore.QSaveFile.commit` does, too.

Returns ``false`` if the rename could not performed atomically (for example, the temporary file and the target file name live on different file systems / volumes / drives.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.rename`, :sip:ref:`~PyQt6.QtCore.QSaveFile`, :sip:ref:`~PyQt6.QtCore.QSaveFile.commit`, :sip:ref:`~PyQt6.QtCore.QFile.rename`.
