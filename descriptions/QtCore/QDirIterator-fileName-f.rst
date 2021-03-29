.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 3125b5656e7220e1a6aa143626e1c891

Returns the file name for the current directory entry, without the path prepended.

This function is convenient when iterating a single directory. When using the :sip:ref:`~PyQt6.QtCore.QDirIterator.IteratorFlags.Subdirectories` flag, you can use :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath` to get the full path.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDirIterator.filePath`, :sip:ref:`~PyQt6.QtCore.QDirIterator.fileInfo`.
