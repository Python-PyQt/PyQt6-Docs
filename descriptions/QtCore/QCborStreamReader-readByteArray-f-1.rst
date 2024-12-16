.. sip:method-description::
    :status: todo
    :pysig: 60467de5baf01ae61b2b674d0e362455
    :realsig: ()
    :digest: e502642864f57e5316457f0d290668ab

Decodes one byte array chunk from the CBOR string and returns it. This function is used for both regular and chunked contents, so the caller must always loop around calling this function, even if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown` is true. The typical use of this function is as follows:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 335-349

The :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readAllByteArray` function implements the above loop and some extra checks.

This function does not perform any type conversions, including from integers or from strings. Therefore, it may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isByteArray` is true; calling it in any other condition is an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readAllByteArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readString`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isByteArray`, readStringChunk().
