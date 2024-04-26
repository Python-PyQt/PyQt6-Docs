.. sip:method-description::
    :status: todo
    :pysig: abb886cd60844075333edf0b76045ae6
    :realsig: (QFileDevice::Permissions) const
    :digest: 01e7b7b7a9df4dfeaeaa4c87f20149c4

Tests for file permissions. The *permissions* argument can be several flags of type QFile::Permissions OR-ed together to check for permission combinations.

On systems where files do not have permissions this function always returns ``true``.

**Note:** The result might be inaccurate on Windows if the :ref:`qfileinfo-ntfs-permissions` check has not been enabled.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 153-157

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isReadable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isWritable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isExecutable`.
