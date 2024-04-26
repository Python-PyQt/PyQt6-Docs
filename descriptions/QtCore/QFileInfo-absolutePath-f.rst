.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 311af72c670a7ca23b381cde7c09ece0

Returns the absolute path of the file system entry this :sip:ref:`~PyQt6.QtCore.QFileInfo` refers to, excluding the entry's name.

On Unix, absolute paths begin with the directory separator ``'/'``. On Windows, absolute paths begin with a drive specification (for example, ``D:/``).

On Windows, the paths of network shares that are not mapped to a drive letter begin with ``//sharename/``.

In contrast to :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalPath` symbolic links or redundant "." or ".." elements are not necessarily removed.

**Warning:** If :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath` is empty the behavior of this function is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.absoluteFilePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.path`, :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalPath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
