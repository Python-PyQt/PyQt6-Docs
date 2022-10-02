.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 9809e70959eb3cb23d5c804a48cfd82e

Returns ``true`` if this object points to a symbolic link; otherwise returns ``false``.

Symbolic links exist on Unix (including macOS and iOS) and Windows (NTFS-symlink) and are typically created by the ``ln -s`` or ``mklink`` commands, respectively.

Unix handles symlinks transparently. Opening a symbolic link effectively opens the :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.

In contrast to :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, false will be returned for shortcuts (``\*.lnk`` files) on Windows and aliases on macOS. Use :sip:ref:`~PyQt6.QtCore.QFileInfo.isShortcut` and :sip:ref:`~PyQt6.QtCore.QFileInfo.isAlias` instead.

**Note:** If the symlink points to a non existing file, :sip:ref:`~PyQt6.QtCore.QFileInfo.exists` returns false.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isShortcut`, :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.
