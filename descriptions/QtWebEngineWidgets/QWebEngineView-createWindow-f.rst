.. sip:method-description::
    :status: todo
    :pysig: cb613500f37b113390ee4a0f375573b8
    :realsig: (QWebEnginePage::WebWindowType)
    :digest: 9681d8e8f69f08042b4fb71ac422f924

This function is called from the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.createWindow` method of the associated :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` each time the page wants to create a new window of the given *type*. For example, when a JavaScript request to open a document in a new window is issued.

**Note:** If the ``createWindow()`` method of the associated page is reimplemented, this method is not called, unless explicitly done so in the reimplementation.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.createWindow`.
