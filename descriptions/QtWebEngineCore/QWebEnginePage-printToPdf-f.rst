.. sip:method-description::
    :status: todo
    :pysig: 0b0c3a9aa9185e34cf2d3bd627ed65c8
    :realsig: (const QString&,const QPageLayout&,const QPageRanges&)
    :digest: 9cfe79e9461aadc7211df510b8b85c0d

Renders the current content of the page into a PDF document and saves it in the location specified in *filePath*. The page size and orientation of the produced PDF document are taken from the values specified in *layout*, while the range of pages printed is taken from *ranges* with the default being printing all pages.

This method issues an asynchronous request for printing the web page into a PDF and returns immediately. To be informed about the result of the request, connect to the signal :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.pdfPrintingFinished`.

If a file already exists at the provided file path, it will be overwritten.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.pdfPrintingFinished`.
