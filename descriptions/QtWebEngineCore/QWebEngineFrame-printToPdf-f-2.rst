.. sip:method-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: 5a4414eb56aadd6013c9f1b588fa4166

Renders the current content of the frame into a PDF document and saves it in the location specified in *filePath*. Printing uses a page size of A4, portrait layout, and includes the full range of pages.

This method issues an asynchronous request for printing the web page into a PDF and returns immediately. To be informed about the result of the request, connect to the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.pdfPrintingFinished` signal.

**Note:** The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.WebAction.Stop` web action can be used to interrupt this asynchronous operation.

If a file already exists at the provided file path, it will be overwritten.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.pdfPrintingFinished`.
