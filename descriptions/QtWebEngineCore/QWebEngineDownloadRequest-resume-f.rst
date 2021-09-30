.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: caf692452287cecd0ea5baf2fedf2f07

Resumes the current download if it was paused or interrupted.

Has no effect if the state is not :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadInProgress` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadInterrupted`. Does not change the state.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.pause`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.isPaused`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.state`.
