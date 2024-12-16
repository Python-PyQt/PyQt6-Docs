.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1df0d9a82107e6ba7b167da7b6e41d89

This signal is emitted when the JavaScript ``window.print()`` method is called on the main frame, or the user pressed the print button of PDF viewer plugin. Typically, the signal handler can simply call :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.printToPdf`.

Since 6.8, this signal is only emitted for the main frame, instead of being emitted for any frame that requests printing.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.printToPdf`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.printRequestedByFrame`.
