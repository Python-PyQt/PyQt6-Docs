.. sip:method-description::
    :status: todo
    :pysig: faee251a718408ee33735c75f47a3158
    :realsig: (QPrinter*)
    :digest: bd8f17168f1cb24e8738b171d58c6a08

Renders the current content of the page into a temporary PDF document, then prints it using *printer*.

The settings for creating and printing the PDF document will be retrieved from the *printer* object.

When finished the signal :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.printFinished` is emitted with the ``true`` for success or ``false`` for failure.

It is the users responsibility to ensure the *printer* remains valid until :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.printFinished` has been emitted.

**Note:** Printing runs on the browser process, which is by default not sandboxed.

**Note:** This function rasterizes the result when rendering onto *printer*. Please consider raising the default resolution of *printer* to at least 300 DPI or using :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.printToPdf` to produce PDF file output more effectively.
