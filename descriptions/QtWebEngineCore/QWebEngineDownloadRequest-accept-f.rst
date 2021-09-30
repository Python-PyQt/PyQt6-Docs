.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a70cc82f15e2a5b105aa5a36d7b4ec72

Accepts the current download request, which will start the download.

If the item is in the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadRequested` state, then it will transition into the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadInProgress` state and the downloading will begin. If the item is in any other state, then nothing will happen.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.isFinished`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.stateChanged`.
