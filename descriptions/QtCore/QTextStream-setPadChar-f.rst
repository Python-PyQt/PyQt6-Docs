.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (QChar)
    :digest: 5ed8a386fa382f40a7cf64a47c0d9f9d

Sets the pad character to *ch*. The default value is the ASCII space character (' '), or QChar(0x20). This character is used to fill in the space in fields when generating text.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qtextstream.py
    :lines: 106-111

The string ``s`` contains:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qtextstream.py
    :lines: 116-116

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream.padChar`, :sip:ref:`~PyQt6.QtCore.QTextStream.setFieldWidth`.
