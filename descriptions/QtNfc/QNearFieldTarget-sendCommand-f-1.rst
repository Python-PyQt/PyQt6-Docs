.. sip:method-description::
    :status: todo
    :pysig: 441602a5b02ffb9b6b62aab85468909a
    :realsig: (const QByteArray&)
    :digest: c0b90e4774287a7498e734d7131de9cc

Sends *command* to the near field target. Returns a request id which can be used to track the completion status of the request. An invalid request id will be returned if the target does not support sending tag type specific commands.

The :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.requestCompleted` signal will be emitted on successful completion of the request; otherwise the :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.error` signal will be emitted.

Once the request completes successfully the response can be retrieved from the :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.requestResponse` function. The response of this request will be a :sip:ref:`~PyQt6.QtCore.QByteArray`.

.. seealso:: :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.requestCompleted`, :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.waitForRequestCompleted`.
