.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 547ce9c5871a437900c129edae583560

Returns true if the type of the current element is an array (that is, if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type` returns :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.Array`). If this function returns true, you may call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.enterContainer` to begin parsing that container.

When the current element is an array, you may also call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown` to find out if the array's size is explicit in the CBOR stream. If it is, that size can be obtained by calling :sip:ref:`~PyQt6.QtCore.QCborStreamReader.length`.

The following example pre-allocates a QVariantList given the array's size for more efficient decoding:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 285-296

**Note:** The code above does not validate that the length is a sensible value. If the input stream reports that the length is 1 billion elements, the above function will try to allocate some 16 GB or more of RAM, which can lead to a crash.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isMap`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.length`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.enterContainer`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.leaveContainer`.
