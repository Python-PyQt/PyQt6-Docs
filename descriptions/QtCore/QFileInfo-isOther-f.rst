.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: dd9ff67d08666c5f3b87f6ff2efb2232

Returns ``true`` if this :sip:ref:`~PyQt6.QtCore.QFileInfo` refers to a file system entry that is *not* a directory, regular file or symbolic link. Otherwise returns ``false``.

If this :sip:ref:`~PyQt6.QtCore.QFileInfo` refers to a nonexistent entry, this method returns ``false``.

If the entry is a dangling symbolic link (the target doesn't exist), this method returns ``false``. For a non-dangling symbolic link, this function returns information about the target, not the symbolic link.

On Unix a special (other) file system entry is a FIFO, socket, character device, or block device. For more details, see the `
                             <https://pubs.opengroup.org/onlinepubs/9699919799/functions/mknod.html>`_ manual page.

On Windows (for historical reasons, see :ref:`qfileinfo-symbolic-links-and-shortcuts`) this method returns ``true`` for ``.lnk`` files.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, QDirListing::IteratorFlag::ExcludeOther.
