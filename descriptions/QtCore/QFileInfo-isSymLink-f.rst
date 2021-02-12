.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 4b1826ace7940053807d93dafbaa456f

Returns ``true`` if this object points to a symbolic link or shortcut; otherwise returns ``false``.

Symbolic links exist on Unix (including macOS and iOS) and Windows and are typically created by the ``ln -s`` or ``mklink`` commands, respectively. Opening a symbolic link effectively opens the :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.

In addition, true will be returned for shortcuts (``\*.lnk`` files) on Windows. This behavior is deprecated and will likely change in a future version of Qt. Opening those will open the ``.lnk`` file itself.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 146-148

**Note:** If the symlink points to a non existing file, :sip:ref:`~PyQt6.QtCore.QFileInfo.exists` returns false.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.symLinkTarget`.
