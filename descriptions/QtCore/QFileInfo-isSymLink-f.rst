.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: dd53284da94647611955b9ad37417994

Returns ``true`` if this object points to a symbolic link, shortcut, or alias; otherwise returns ``false``.

Symbolic links exist on Unix (including macOS and iOS) and Windows and are typically created by the ``ln -s`` or ``mklink`` commands, respectively. Opening a symbolic link effectively opens the :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.

In addition, true will be returned for shortcuts (``\*.lnk`` files) on Windows, and aliases on macOS. This behavior is deprecated and will likely change in a future version of Qt. Opening a shortcut or alias will open the ``.lnk`` or alias file itself.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 146-148

**Note:** :sip:ref:`~PyQt6.QtCore.QFileInfo.exists` returns ``true`` if the symlink points to an existing target, otherwise it returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.
