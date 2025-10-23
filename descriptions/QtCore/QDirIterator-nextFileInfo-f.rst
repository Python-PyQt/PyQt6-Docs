.. sip:method-description::
    :status: todo
    :pysig: e8c984744982164ad826179be740c9af
    :realsig: ()
    :digest: 5a2ffe50508d1a14db89f229e986ae2a

Advances the iterator to the next entry, and returns the file info of this new entry. If :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext` returns ``false``, this function does nothing, and returns an empty :sip:ref:`~PyQt6.QtCore.QFileInfo`. Ideally you should always call :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext` before calling this method.

You can call :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName` or :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath` to get the current entry's file name or path, or :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo` to get a :sip:ref:`~PyQt6.QtCore.QFileInfo` for the current entry.

Call :sip:ref:`~PyQt6.QtCore.QDirIterator.next` instead of nextFileInfo() when all you need is the :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.hasNext`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileName`, :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo`.
