.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qint64,qint64)
    :digest: d7d0fd41888c9b5b79f2a12051ad6582

This signal is emitted to indicate the progress of the download part of this network request, if there's any. If there's no download associated with this request, this signal will be emitted once with 0 as the value of both *bytesReceived* and *bytesTotal*.

The *bytesReceived* parameter indicates the number of bytes received, while *bytesTotal* indicates the total number of bytes expected to be downloaded. If the number of bytes to be downloaded is not known, *bytesTotal* will be -1.

The download is finished when *bytesReceived* is equal to *bytesTotal*. At that time, *bytesTotal* will not be -1.

Note that the values of both *bytesReceived* and *bytesTotal* may be different from size(), the total number of bytes obtained through read() or readAll(), or the value of the header(ContentLengthHeader). The reason for that is that there may be protocol overhead or the data may be compressed during the download.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.uploadProgress`, bytesAvailable().
