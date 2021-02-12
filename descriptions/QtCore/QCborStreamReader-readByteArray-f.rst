.. sip:method-description::
    :status: todo
    :pysig: 9470cd47385e34201c6eff3f2050ab81
    :realsig: ()
    :digest: 814da8f243a96558d2db60f48de8ea1f

Decodes one byte array chunk from the CBOR string and returns it. This function is used for both regular and chunked contents, so the caller must always loop around calling this function, even if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown` has is true. The typical use of this function is as follows:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 335-349

This function does not perform any type conversions, including from integers or from strings. Therefore, it may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isByteArray` is true; calling it in any other condition is an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readString`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isByteArray`, readStringChunk().
