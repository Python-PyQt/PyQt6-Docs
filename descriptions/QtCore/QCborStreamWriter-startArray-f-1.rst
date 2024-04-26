.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (quint64)
    :digest: a011082616f9d5783a40292a0b68c771

This is an overloaded function.

Starts a CBOR Array with explicit length of *count* items in the CBOR stream. Each :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startArray` call must be paired with one :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endArray` call and the current CBOR element extends until the end of the array.

The array created by this function has an explicit length and therefore exactly *count* items must be added to the CBOR stream. Adding fewer or more items will result in failure during :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endArray` and the CBOR stream will be corrupt. However, explicit-length arrays are required by canonical CBOR encoding.

The following example appends all strings found in the QStringList passed as input:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 223-229

**Size limitations**: The parameter to this function is quint64, which would seem to allow up to 2\ :sup:`64`-1 elements in the array. However, both :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` and :sip:ref:`~PyQt6.QtCore.QCborStreamReader` are currently limited to 2\ :sup:`32`-2 items on 32-bit systems and 2\ :sup:`64`-2 items on 64-bit ones. Also note that QCborArray is currently limited to 2\ :sup:`27` elements on 32-bit platforms and 2\ :sup:`59` elements on 64-bit ones.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startMap`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown`.
