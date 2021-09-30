.. sip:signal-description::
    :status: todo
    :pysig: d3a634956afa25751559c99ea6f53480
    :realsig: (QWebEngineDownloadRequest*)
    :digest: 76b73dd5b5969cc5a99eb602c5ec5c6e

This signal is emitted whenever a download has been triggered. The *download* argument holds the state of the download. The download has to be explicitly accepted with :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.accept` or it will be cancelled by default. The download item is parented by the profile. If it is not accepted, it will be deleted immediately after the signal emission. This signal cannot be used with a queued connection.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.download`.
