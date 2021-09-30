.. sip:method-description::
    :status: todo
    :pysig: d8220d06419a5e26b1941083801d8e34
    :realsig: ()
    :digest: d9dd821e5afecdfc04640cfacc15bfd5

Starts reading NDEF messages stored on the near field target. Returns a request id which can be used to track the completion status of the request. An invalid request id will be returned if the target does not support reading NDEF messages.

An :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.ndefMessageRead` signal will be emitted for each NDEF message. The :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.requestCompleted` signal will be emitted was all NDEF messages have been read. The :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.error` signal is emitted if an error occurs.

**Note:** An attempt to read an NDEF message from a tag, that is in INITIALIZED state as defined by NFC Forum, will fail with the :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.Error.NdefReadError`, as the tag is formatted to support NDEF but does not contain a message yet.
