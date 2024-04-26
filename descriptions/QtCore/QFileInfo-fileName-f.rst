.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 1e444bb2f76df80328d3653d4ff6df89

Returns the name of the file system entry this :sip:ref:`~PyQt6.QtCore.QFileInfo` refers to, excluding the path.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 110-111

**Note:** If this :sip:ref:`~PyQt6.QtCore.QFileInfo` is given a path ending with a directory separator ``'/'``, the entry's name part is considered empty.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`, :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.baseName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.suffix`.
