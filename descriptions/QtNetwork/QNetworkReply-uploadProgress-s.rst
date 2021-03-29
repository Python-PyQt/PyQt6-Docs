.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qint64,qint64)
    :digest: e0372c7bca2b466df291d2e37167de64

This signal is emitted to indicate the progress of the upload part of this network request, if there's any. If there's no upload associated with this request, this signal will not be emitted.

The *bytesSent* parameter indicates the number of bytes uploaded, while *bytesTotal* indicates the total number of bytes to be uploaded. If the number of bytes to be uploaded could not be determined, *bytesTotal* will be -1.

The upload is finished when *bytesSent* is equal to *bytesTotal*. At that time, *bytesTotal* will not be -1.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.downloadProgress`.
