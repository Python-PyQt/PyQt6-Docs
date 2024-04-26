.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: ()
    :digest: 39626a4c74a27d587dcfed71d97d924b

Decodes the current text string and returns it. If the string is chunked, this function will iterate over all chunks and concatenate them. If an error happens, this function returns a default-constructed QString(), but that may not be distinguishable from certain empty text strings. Instead, check :sip:ref:`~PyQt6.QtCore.QCborStreamReader.lastError` to determine if an error has happened.

This function does not perform any type conversions, including from integers or from byte arrays. Therefore, it may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isString` returned true; calling it in any other condition is an error.

**Note:** This function cannot be resumed. That is, this function should not be used in contexts where the CBOR data may still be received, for example from a socket or pipe. It should only be used when the full data has already been received and is available in the input :sip:ref:`~PyQt6.QtCore.QByteArray` or :sip:ref:`~PyQt6.QtCore.QIODevice`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readString`, readStringChunk(), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isString`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readAllByteArray`.
