.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: c9e13f3969e5c04b62e66530f2da4b47

Appends a CBOR Null value to the stream. This function is equivalent to (and implemented as):

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 205-205

.. seealso:: append(std::nullptr_t), append(QCborSimpleType), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isNull`.
