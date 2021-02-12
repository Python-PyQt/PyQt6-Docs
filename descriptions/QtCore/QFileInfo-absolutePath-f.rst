.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: a2945f1be5be47ccb62aa83e07245db6

Returns a file's path absolute path. This doesn't include the file name.

On Unix the absolute path will always begin with the root, '/', directory. On Windows this will always begin 'D:/' where D is a drive letter, except for network shares that are not mapped to a drive letter, in which case the path will begin '//sharename/'.

In contrast to :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalPath` symbolic links or redundant "." or ".." elements are not necessarily removed.

**Warning:** If :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath` is empty the behavior of this function is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.absoluteFilePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.path`, :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalPath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
