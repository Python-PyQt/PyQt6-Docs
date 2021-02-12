.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 7b4cf76d2efb95f44e32c5aed75a2723

Returns an absolute path including the file name.

The absolute path name consists of the full path and the file name. On Unix this will always begin with the root, '/', directory. On Windows this will always begin 'D:/' where D is a drive letter, except for network shares that are not mapped to a drive letter, in which case the path will begin '//sharename/'. :sip:ref:`~PyQt6.QtCore.QFileInfo` will uppercase drive letters. Note that :sip:ref:`~PyQt6.QtCore.QDir` does not do this. The code snippet below shows this.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py

This function returns the same as :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, unless :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative` is true. In contrast to :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalFilePath`, symbolic links or redundant "." or ".." elements are not necessarily removed.

**Warning:** If :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath` is empty the behavior of this function is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalFilePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
