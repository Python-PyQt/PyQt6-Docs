.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 698da88e7b5a8c0173de270f31255c63

Returns the name of the file, excluding the path.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 110-111

Note that, if this :sip:ref:`~PyQt6.QtCore.QFileInfo` object is given a path ending in a slash, the name of the file is considered empty.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`, :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.baseName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.suffix`.
