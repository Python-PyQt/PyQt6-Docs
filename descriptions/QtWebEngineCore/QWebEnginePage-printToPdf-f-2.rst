.. sip:method-description::
    :status: todo
    :pysig: 27a49a5bec2181b897741f72019215dc
    :realsig: (const QString&, const QPageLayout&, const QPageRanges&)
    :digest: 6f598658c91db89a9b6ca0bdcaf2a239

Renders the current content of the page into a PDF document and saves it in the location specified in *filePath*. The page size and orientation of the produced PDF document are taken from the values specified in *layout*, while the range of pages printed is taken from *ranges* with the default being printing all pages.

This method issues an asynchronous request for printing the web page into a PDF and returns immediately. To be informed about the result of the request, connect to the signal :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.pdfPrintingFinished`.

**Note:** The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.WebAction.Stop` web action can be used to interrupt this asynchronous operation.

If a file already exists at the provided file path, it will be overwritten.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.pdfPrintingFinished`.
