.. sip:method-description::
    :status: todo
    :pysig: 9e6cf921ea536b15e55517c3ea382b7c
    :realsig: (char) const
    :digest: 4763594e5cfdfcb1101f9856435d0d1e

Returns a hex encoded copy of the byte array.

The hex encoding uses the numbers 0-9 and the letters a-f.

If *separator* is not '``\0``', the separator character is inserted between the hex bytes.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 488-490

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.fromHex`.
