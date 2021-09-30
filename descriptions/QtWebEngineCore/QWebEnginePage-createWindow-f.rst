.. sip:method-description::
    :status: todo
    :pysig: 8349a95ad1bcf28150cb261f4cb1459c
    :realsig: (QWebEnginePage::WebWindowType)
    :digest: e1559117c223f0c905caf8507fb15190

This function is called to create a new window of the specified *type*. For example, when a JavaScript program requests to open a document in a new window.

If the new window can be created, the new window's :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` is returned; otherwise a null pointer is returned.

If the view associated with the web page is a :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView` object, then the default implementation forwards the request to :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.createWindow`; otherwise it returns a null pointer.

If this call is not implemented or does not return a new page, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.newWindowRequested` is emitted to handle the request.

**Note:** In the cases when the window creation is being triggered by JavaScript, apart from reimplementing this method the application must also set :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineSettings.WebAttribute.JavascriptCanOpenWindows` to ``true`` in order for the method to get called.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.createWindow`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.newWindowRequested`.
