.. sip:signal-description::
    :status: todo
    :pysig: 27cba0796e8a74ae1e96ad538d10dfe6
    :realsig: (QWebEngineNewWindowRequest&)
    :digest: f6c53592e6ae7bf756cc70084b8bca9d

This signal is emitted when *request* is issued to load a page in a separate web engine window. This can either be because the current page requested it explicitly through a JavaScript call to ``window.open``, or because the user clicked on a link while holding Shift, Ctrl, or a built-in combination that triggers the page to open in a new window.

The signal is handled by calling openIn() with the new page on the request. If this signal is not handled, the requested load will fail.

**Note:** This signal is not emitted if :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.createWindow` handled the request first.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.createWindow`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineNewWindowRequest.openIn`.
