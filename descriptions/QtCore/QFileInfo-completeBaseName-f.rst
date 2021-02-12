.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 7cb117e233391431f2402bcc7b59af17

Returns the complete base name of the file without the path.

The complete base name consists of all characters in the file up to (but not including) the *last* '.' character.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 128-129

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.suffix`, :sip:ref:`~PyQt6.QtCore.QFileInfo.completeSuffix`, :sip:ref:`~PyQt6.QtCore.QFileInfo.baseName`.
