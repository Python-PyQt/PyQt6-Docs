.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (QStringView)
    :digest: 2c2934204de5f9a4ef860dadc7587010

This is an overloaded function.

Appends the text string *str* to the stream, creating a CBOR Text String value. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` will attempt to write the entire string in one chunk.

The following example writes an arbitrary QString to the stream:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 127-130

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isString`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.readString`.
