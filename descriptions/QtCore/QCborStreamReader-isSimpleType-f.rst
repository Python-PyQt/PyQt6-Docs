.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 79bf6e38492a17fafcc7b55ac9df55b6

Returns true if the type of the current element is any CBOR simple type, including a boolean value (true and false) as well as null and undefined. To find out which simple type this is, call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toSimpleType`. Alternatively, to test for one specific simple type, call the overload that takes a :sip:ref:`~PyQt6.QtCore.QCborSimpleType` parameter.

CBOR simple types are types that do not carry extra value. There are 255 possibilities, but there are currently only four values that have defined meaning. Code is not expected to cope with unknown simple types and may simply discard the stream as invalid if it finds an unknown one.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborSimpleType`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, isSimpleType(QCborSimpleType), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toSimpleType`.
