.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: ()
    :digest: 8428c7febbba789cf95975081d273c92

Advances the iterator to the next entry, and returns the file path of this new entry. You should first check :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext` before using this method, to avoid unexpected results.

You can call :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName` or :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath` to get the current entry's file name or path, or :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo` to get a :sip:ref:`~PyQt6.QtCore.QFileInfo` for the current entry.

Call :sip:ref:`~PyQt6.QtCore.QDirIterator.nextFileInfo` instead of next() if you're interested in the :sip:ref:`~PyQt6.QtCore.QFileInfo`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.nextFileInfo`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName`, :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo`.
