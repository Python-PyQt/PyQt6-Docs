.. sip:method-description::
    :status: todo
    :pysig: aeaf3eb3aa263437ce2b8fcdd983fc37
    :realsig: (qsizetype) const
    :digest: 03ca505febc6b2711cd295663b996e61

Returns a copy of this byte array repeated the specified number of *times*.

If *times* is less than 1, an empty byte array is returned.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 483-484
