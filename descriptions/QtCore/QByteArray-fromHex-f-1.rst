.. sip:method-description::
    :status: todo
    :pysig: 65ab462c2f62ed6c1874eabd35838135
    :realsig: (const QByteArray&)
    :digest: 6c57135b05c30bce0df89ed694540ae0

Returns a decoded copy of the hex encoded array *hexEncoded*. Input is not checked for validity; invalid characters in the input are skipped, enabling the decoding process to continue with subsequent characters.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 443-444

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.toHex`.
