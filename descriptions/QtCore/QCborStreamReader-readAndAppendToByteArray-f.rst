.. sip:method-description::
    :status: todo
    :pysig: 818ceb9f7882cf71214966cf00526abf
    :realsig: (QByteArray&)
    :digest: 71ff67096272d83e9885228c52ae8e41

Decodes the current byte string and appends to *dst*. If the string is chunked, this function will iterate over all chunks and concatenate them. If an error happens during decoding, other chunks that could be decoded successfully may have been written to *dst* nonetheless. Returns ``true`` if the decoding happened without errors, ``false`` otherwise.

This function does not perform any type conversions, including from integers or from strings. Therefore, it may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isByteArray` is true; calling it in any other condition is an error.

**Note:** This function cannot be resumed. That is, this function should not be used in contexts where the CBOR data may still be received, for example from a socket or pipe. It should only be used when the full data has already been received and is available in the input :sip:ref:`~PyQt6.QtCore.QByteArray` or :sip:ref:`~PyQt6.QtCore.QIODevice`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readByteArray`, readStringChunk(), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isByteArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readAndAppendToString`.
