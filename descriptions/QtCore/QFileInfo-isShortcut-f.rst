.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 8ede8719ae39e16fd89e8cc7f40c4602

Returns ``true`` if this object points to a shortcut; otherwise returns ``false``.

Shortcuts only exist on Windows and are typically ``.lnk`` files. For instance, true will be returned for shortcuts (``\*.lnk`` files) on Windows, but false will be returned on Unix (including macOS and iOS).

The shortcut (.lnk) files are treated as regular files. Opening those will open the ``.lnk`` file itself. In order to open the file a shortcut references to, it must uses :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget` on a shortcut.

**Note:** Even if a shortcut (broken shortcut) points to a non existing file,  returns true.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymbolicLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.
