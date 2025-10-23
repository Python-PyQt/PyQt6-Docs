.. sip:method-description::
    :status: todo
    :pysig: 5b5f0037effa64dcfdc4b07c83e631b9
    :realsig: (QCborSimpleType)
    :digest: bb9519719540962ed602b63c6ad0c17f

Appends the CBOR simple type *st* to the stream, creating a CBOR Simple Type value. In the following example, we write the simple type for Null as well as for type 32, which Qt has no support for.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 150-151

**Note:** Using Simple Types for which there is no specification can lead to validation errors by the remote receiver. In addition, simple type values 24 through 31 (inclusive) are reserved and must not be used.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isSimpleType`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toSimpleType`.
