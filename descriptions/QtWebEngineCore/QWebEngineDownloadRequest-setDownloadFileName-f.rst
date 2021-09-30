.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 0e30164ebfb8a4210ff30306895b54b7

Sets *fileName* as the file name to download the file to.

The download file name can only be set in response to the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.downloadRequested` signal before the download is accepted. Past that point, this function has no effect on the download item's state.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.downloadFileName`.
