.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 5c939b48b0a868fa7df723ff3224be22

Sets *directory* as the directory path to download the file to.

The download directory path can only be set in response to the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.downloadRequested` signal before the download is accepted. Past that point, this function has no effect on the download item's state.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.downloadDirectory`.
