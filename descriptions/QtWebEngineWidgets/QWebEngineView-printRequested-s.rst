.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 7d87db534f34f7737834ceae3d14b334

This signal is emitted when the JavaScript ``window.print()`` method is called or the user pressed the print button of PDF viewer plugin. Typically, the signal handler can simply call :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.print`.

Since 6.8, this signal is only emitted for the main frame, instead of being emitted for any frame that requests printing.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.printRequestedByFrame`, :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.print`.
