.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: ()
    :digest: b9b94a45d0fc94a2b0964fffe99cd540

Advances the iterator to the next entry, and returns the file path of this new entry. If :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext` returns ``false``, this function does nothing, and returns an empty QString. Ideally you should always call :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext` before calling this method.

You can call :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName` or :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath` to get the current entry's file name or path, or :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo` to get a :sip:ref:`~PyQt6.QtCore.QFileInfo` for the current entry.

Call :sip:ref:`~PyQt6.QtCore.QDirIterator.nextFileInfo` instead of next() if you're interested in the :sip:ref:`~PyQt6.QtCore.QFileInfo`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.nextFileInfo`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName`, :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo`.
