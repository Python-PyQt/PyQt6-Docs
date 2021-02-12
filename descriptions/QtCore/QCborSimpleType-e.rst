.. sip:enum-description::
    :status: todo
    :digest: d6eed41e2dbf05acffa4120f8b0c11b7

This enum contains the possible "Simple Types" for CBOR. Simple Types range from 0 to 255 and are types that carry no further value.

The following values are currently known:

Qt CBOR API supports encoding and decoding any Simple Type, whether one of those above or any other value.

Applications should only use further values if a corresponding specification has been published, otherwise interpretation and validation by the remote may fail. Values 24 to 31 are reserved and must not be used.

The current authoritative list is maintained by IANA in the `Simple Values registry <https://www.iana.org/assignments/cbor-simple-values/cbor-simple-values.xml>`_.

.. seealso:: QCborStreamWriter::append(QCborSimpleType), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isSimpleType`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toSimpleType`, QCborValue::isSimpleType(), QCborValue::toSimpleType().
