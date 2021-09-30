.. sip:method-description::
    :status: todo
    :pysig: c38b37308fdf8bd72020151fbf63f774
    :realsig: (const QString&,QWebEngineDownloadRequest::SavePageFormat) const
    :digest: 9e917dae5fd8460cf2fc719ad32f2b67

Save the currently loaded web page to disk.

The web page is saved to *filePath* in the specified *format*.

This is a short cut for the following actions:

* Trigger the Save web action.

* Accept the next download item and set the specified file path and save format.

This function issues an asynchronous download request for the web page and returns immediately.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.SavePageFormat`.
