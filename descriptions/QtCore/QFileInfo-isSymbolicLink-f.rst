.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 5c435d3058b0af5aa22452031704423b

Returns ``true`` if this object points to a symbolic link; otherwise returns ``false``.

Symbolic links exist on Unix (including macOS and iOS) and Windows (NTFS-symlink) and are typically created by the ``ln -s`` or ``mklink`` commands, respectively.

Unix handles symlinks transparently. Opening a symbolic link effectively opens the :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.

In contrast to :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, false will be returned for shortcuts (``\*.lnk`` files) on Windows and aliases on macOS. Use :sip:ref:`~PyQt6.QtCore.QFileInfo.isShortcut` and :sip:ref:`~PyQt6.QtCore.QFileInfo.isAlias` instead.

**Note:** :sip:ref:`~PyQt6.QtCore.QFileInfo.exists` returns ``true`` if the symlink points to an existing target, otherwise it returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isShortcut`, :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.
