.. sip:method-description::
    :status: todo
    :pysig: dd3e2c43701c76e75d7635bb80ca4ee6
    :realsig: (QByteArray::Base64Options) const
    :digest: b97f26c994db580ab6079167f81688e3

Returns a copy of the byte array, encoded using the options *options*.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 375-382

The algorithm used to encode Base64-encoded data is defined in RFC 4648.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.fromBase64`.
