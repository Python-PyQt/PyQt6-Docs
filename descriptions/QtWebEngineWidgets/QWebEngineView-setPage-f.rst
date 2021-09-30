.. sip:method-description::
    :status: todo
    :pysig: 30ad8a949a45ea99ef5556c72d0c4346
    :realsig: (QWebEnginePage*)
    :digest: b40863b9f876a09723df0cf67ef70a31

Makes *page* the new web page of the web view.

The parent :sip:ref:`~PyQt6.QtCore.QObject` of the provided page remains the owner of the object. If the current page is a child of the web view, it will be deleted.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.page`.
