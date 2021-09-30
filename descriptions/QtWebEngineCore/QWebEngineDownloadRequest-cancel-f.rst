.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 30d343da9a89035226d426edf9f42c2e

Cancels the current download.

If the item is in the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadInProgress` state, then it will transition into the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadCancelled` state, the downloading will stop, and partially downloaded files will be deleted from disk.

If the item is in the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadCompleted` state, then nothing will happen. If the item is in any other state, then it will transition into the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadCancelled` state without further effect.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.isFinished`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.stateChanged`.
