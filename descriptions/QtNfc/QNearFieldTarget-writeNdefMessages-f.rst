.. sip:method-description::
    :status: todo
    :pysig: 86f034ddaf63853211b39e00ebf6572c
    :realsig: (const QList<QNdefMessage>&)
    :digest: 4e129e09850b5a1e6988160c2a6797e7

Writes the NDEF messages in *messages* to the target. Returns a request id which can be used to track the completion status of the request. An invalid request id will be returned if the target does not support reading NDEF messages.

The :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.requestCompleted` signal will be emitted when the write operation completes successfully; otherwise the :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.error` signal is emitted.
