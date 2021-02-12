.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: ()
    :digest: 4d047b5360fe9a4afa815dba870a74ed

Advances the iterator to the next entry, and returns the file path of this new entry. If :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext` returns ``false``, this function does nothing, and returns an empty QString.

You can call :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName` or :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath` to get the current entry file name or path, or :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo` to get a :sip:ref:`~PyQt6.QtCore.QFileInfo` for the current entry.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName`, :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo`.
