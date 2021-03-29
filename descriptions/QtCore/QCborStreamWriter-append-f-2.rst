.. sip:method-description::
    :status: todo
    :pysig: cc0ea0b761b7fcad614b4d8cf87842d5
    :realsig: (QCborKnownTags)
    :digest: 42299f47e26e636214efbc2c85ac14fb

This is an overloaded function.

Appends the CBOR tag *tag* to the stream, creating a CBOR Tag value. All tags must be followed by another type which they provide meaning for.

In the following example, we append a CBOR Tag 1 (Unix ``time_t``) and an integer representing the current time to the stream, obtained using the ``time()`` function:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 142-146

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isTag`, QCborStreamReader::toTag().
