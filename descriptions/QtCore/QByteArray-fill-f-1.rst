.. sip:method-description::
    :status: todo
    :pysig: 43eeb45632e8b458f67c5214ad0b5db8
    :realsig: (char,qsizetype)
    :digest: dbedbcbc157fd501c5fdd4b618cee20a

Sets every byte in the byte array to *ch*. If *size* is different from -1 (the default), the byte array is resized to size *size* beforehand.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 173-178

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.resize`.
