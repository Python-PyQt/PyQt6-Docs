.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 7b3b2f837de0f8b9b4c66ee03bdf1e63

Starts a CBOR Map with indeterminate length in the CBOR stream. Each  call must be paired with one :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endMap` call and the current CBOR element extends until the end of the map.

The map created by this function has no explicit length. Instead, its length is implied by the elements contained in it. Note, however, that use of indeterminate-length maps is not compliant with canonical CBOR encoding (canonical encoding also requires keys to be unique and in sorted order).

The following example appends elements from the list of int and string pairs passed as input:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 233-241

.. seealso:: startMap(quint64), :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endMap`, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isMap`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown`.
