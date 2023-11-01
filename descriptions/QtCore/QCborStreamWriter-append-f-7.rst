.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: fa8ee4ca6f2f429231ccc8167180d9ac

This is an overloaded function.

Appends the byte array *ba* to the stream, creating a CBOR Byte String value. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` will attempt to write the entire string in one chunk.

The following example will load and append the contents of a file to the stream:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 114-119

As the example shows, unlike JSON, CBOR requires no escaping for binary content.

.. seealso:: appendByteString(), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isByteArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readByteArray`.
