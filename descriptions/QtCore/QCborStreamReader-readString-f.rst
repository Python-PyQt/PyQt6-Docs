.. sip:method-description::
    :status: todo
    :pysig: df602279bdf635901cfa6e3d0fc19a48
    :realsig: ()
    :digest: d597c9cdc8f7a3a6ea2a1fcb0057214a

Decodes one string chunk from the CBOR string and returns it. This function is used for both regular and chunked string contents, so the caller must always loop around calling this function, even if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown` is true. The typical use of this function is as follows:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 317-331

The :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readAllString` function implements the above loop and some extra checks.

This function does not perform any type conversions, including from integers or from byte arrays. Therefore, it may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isString` returned true; calling it in any other condition is an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readAllString`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readByteArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isString`, readStringChunk().
