.. sip:signal-description::
    :status: todo
    :pysig: 326e42bf2b72653244d70ec9bcbb7415
    :realsig: (QNetworkReply::NetworkError)
    :digest: 92ec5ff0deed5d120dbdadd3d2a0a860

This signal is emitted when the reply detects an error in processing. The :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.finished` signal will probably follow, indicating that the connection is over.

The *code* parameter contains the code of the error that was detected. Call errorString() to obtain a textual representation of the error condition.

**Note:** Do not delete the object in the slot connected to this signal. Use deleteLater().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.error`, errorString().
