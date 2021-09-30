.. sip:class-description::
    :status: todo
    :brief: NFC NDEF record
    :digest: a0ce58f64e066c5949ddf1a8d0140fe5

The :sip:ref:`~PyQt6.QtNfc.QNdefRecord` class provides an NFC NDEF record.

:sip:ref:`~PyQt6.QtNfc.QNdefRecord` and derived classes are used to parse the contents of :sip:ref:`~PyQt6.QtNfc.QNdefMessage` and create new NDEF messages.

Use :sip:ref:`~PyQt6.QtNfc.QNdefRecord.typeNameFormat` and :sip:ref:`~PyQt6.QtNfc.QNdefRecord.setTypeNameFormat` to get and set the type name format of the NDEF record.

Use :sip:ref:`~PyQt6.QtNfc.QNdefRecord.type` and :sip:ref:`~PyQt6.QtNfc.QNdefRecord.setType` to get and set the type of the NDEF record.

Use :sip:ref:`~PyQt6.QtNfc.QNdefRecord.id` and :sip:ref:`~PyQt6.QtNfc.QNdefRecord.setId` to get and set the id of the NDEF record.

Use :sip:ref:`~PyQt6.QtNfc.QNdefRecord.payload` and :sip:ref:`~PyQt6.QtNfc.QNdefRecord.setPayload` to get and set the NDEF record payload. :sip:ref:`~PyQt6.QtNfc.QNdefRecord.isEmpty` can be used to test if the payload is empty.

:sip:ref:`~PyQt6.QtNfc.QNdefRecord` is an implicitly shared class. This means you can efficiently convert between :sip:ref:`~PyQt6.QtNfc.QNdefRecord` and specialized record classes. The isRecordType() template function can be used to test if a conversion is possible. The following example shows how to test if a :sip:ref:`~PyQt6.QtNfc.QNdefRecord` is an NFC RTD Text record and extract the text information from it.

.. literalinclude:: ../../../snippets/qtconnectivity-src-nfc-doc-snippets-nfc.py
    :lines: 65-69

.. _qndefrecord-creating-specialized-ndef-record-classes:

Creating Specialized NDEF Record Classes
----------------------------------------

Specialized NDEF record classes can be easily created with the Q_DECLARE_NDEF_RECORD() and Q_DECLARE_ISRECORDTYPE_FOR_NDEF_RECORD() macros. The following example shows the class declaration of the hypothetical *example.com:f* record type that encapsulates a single int property foo.

.. literalinclude:: ../../../snippets/qtconnectivity-src-nfc-doc-snippets-nfc.py
    :lines: 74-84

The developer only needs to provide implementations for the ``foo()`` and ``setFoo()`` functions that parse and set the contents of the NDEF record's payload.
