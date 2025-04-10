.. sip:class-description::
    :status: todo
    :brief: NFC NDEF message
    :digest: 954e74a58fefe85be64b333dbf767fe4

The :sip:ref:`~PyQt6.QtNfc.QNdefMessage` class provides an NFC NDEF message.

A :sip:ref:`~PyQt6.QtNfc.QNdefMessage` is a collection of 0 or more QNdefRecords. :sip:ref:`~PyQt6.QtNfc.QNdefMessage` inherits from QList<QNdefRecord> and therefore the standard QList functions can be used to manipulate the NDEF records in the message.

NDEF messages can be parsed from a byte array conforming to the NFC Data Exchange Format technical specification by using the fromByteArray() static function. Conversely QNdefMessages can be converted into a byte array with the toByteArray() function.
