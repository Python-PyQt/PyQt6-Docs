.. sip:method-description::
    :status: todo
    :pysig: e8c984744982164ad826179be740c9af
    :realsig: ()
    :digest: 9fafcb2d4bad3a50505504f8e08de5c4

Advances the iterator to the next entry, and returns the file info of this new entry. If :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext` returns ``false``, this function does nothing, and returns an empty :sip:ref:`~PyQt6.QtCore.QFileInfo`.

You can call :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName` or :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath` to get the current entry's file name or path, or :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo` to get a :sip:ref:`~PyQt6.QtCore.QFileInfo` for the current entry.

Call :sip:ref:`~PyQt6.QtCore.QDirIterator.next` instead of  when all you need is the :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName`, :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo`.
