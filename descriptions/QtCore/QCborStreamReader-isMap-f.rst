.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: d2062433d5cf9384790aa5099905e8b7

Returns true if the type of the current element is a map (that is, if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type` returns :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.Map`). If this function returns true, you may call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.enterContainer` to begin parsing that container.

When the current element is a map, you may also call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown` to find out if the map's size is explicit in the CBOR stream. If it is, that size can be obtained by calling :sip:ref:`~PyQt6.QtCore.QCborStreamReader.length`.

The following example pre-allocates a QVariantMap given the map's size for more efficient decoding:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 300-313

The example above uses a function called ``readElementAsString`` to read the map's keys and obtain a string. That is because CBOR maps may contain any type as keys, not just strings. User code needs to either perform this conversion, reject non-string keys, or instead use a different container besides QVariantMap and QVariantHash. For example, if the map is expected to contain integer keys, which is recommended as it reduces stream size and parsing, the correct container would be ``\l{QMap}<int, QVariant>`` or ``\l{QHash}<int, QVariant>``.

**Note:** The code above does not validate that the length is a sensible value. If the input stream reports that the length is 1 billion elements, the above function will try to allocate some 24 GB or more of RAM, which can lead to a crash.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.length`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.enterContainer`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.leaveContainer`.
