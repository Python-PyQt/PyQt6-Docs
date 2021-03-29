.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (quint64)
    :digest: 6b109715c4edaa3719e23ff77f5a1ff2

This is an overloaded function.

Starts a CBOR Map with explicit length of *count* items in the CBOR stream. Each :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startMap` call must be paired with one :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endMap` call and the current CBOR element extends until the end of the map.

The map created by this function has an explicit length and therefore exactly *count* pairs of items must be added to the CBOR stream. Adding fewer or more items will result in failure during :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endMap` and the CBOR stream will be corrupt. However, explicit-length map are required by canonical CBOR encoding.

The following example appends all strings found in the QMap passed as input:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 245-253

**Size limitations**: The parameter to this function is quint64, which would seem to allow up to 2\ :sup:`64`-1 pairs in the map. However, both :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` and :sip:ref:`~PyQt6.QtCore.QCborStreamReader` are currently limited to 2\ :sup:`31`-1 items on 32-bit systems and 2\ :sup:`63`-1 items on 64-bit ones. Also note that QCborMap is currently limited to 2\ :sup:`26` elements in any platform.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startMap`, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endMap`, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isMap`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown`.
