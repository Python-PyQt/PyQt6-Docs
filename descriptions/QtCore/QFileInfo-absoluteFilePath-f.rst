.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 21247839e5058b5228e33731f2b3794c

Returns the absolute full path to the file system entry this :sip:ref:`~PyQt6.QtCore.QFileInfo` refers to, including the entry's name.

On Unix, absolute paths begin with the directory separator ``'/'``. On Windows, absolute paths begin with a drive specification (for example, ``D:/``).

On Windows, the paths of network shares that are not mapped to a drive letter begin with ``//sharename/``.

:sip:ref:`~PyQt6.QtCore.QFileInfo` will uppercase drive letters. Note that :sip:ref:`~PyQt6.QtCore.QDir` does not do this. The code snippet below shows this.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py

This function returns the same as :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, unless :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative` is true. In contrast to :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalFilePath`, symbolic links or redundant "." or ".." elements are not necessarily removed.

**Warning:** If :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath` is empty the behavior of this function is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalFilePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
