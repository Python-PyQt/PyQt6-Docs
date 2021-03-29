.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: b9fee33e380e32ccb6a6796c23b3c981

Returns the type name of the filesystem.

This is a platform-dependent function, and filesystem names can vary between different operating systems. For example, on Windows filesystems they can be named ``NTFS``, and on Linux they can be named ``ntfs-3g`` or ``fuseblk``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStorageInfo.name`.
