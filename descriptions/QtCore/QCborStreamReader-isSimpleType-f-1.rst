.. sip:method-description::
    :status: todo
    :pysig: bdbb89a89adf627ca47475fa4dfcc9cc
    :realsig: (QCborSimpleType) const
    :digest: a9be4fa28ff4e10ebcbfd2dcea52116f

Returns true if the type of the current element is the simple type *st*, false otherwise. If this function returns true, then :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toSimpleType` will return *st*.

CBOR simple types are types that do not carry extra value. There are 255 possibilities, but there are currently only four values that have defined meaning. Code is not expected to cope with unknown simple types and may simply discard the stream as invalid if it finds an unknown one.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborSimpleType`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isSimpleType`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toSimpleType`.
