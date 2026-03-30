.. sip:method-description::
    :status: todo
    :pysig: 54cf6951275915805c5782f93c0a96b5
    :realsig: (const QByteArray&, const QString&, const QUrl&)
    :digest: 63ad19b7561fc82b2642f87bf1e32e52

Sets the content of the web view to *data*. If the *mimeType* argument is empty, it is assumed that the content is ``text/plain,charset=US-ASCII``.

External objects referenced in the content are located relative to *baseUrl*. For external objects with relative URLs to be loaded, ``baseUrl`` cannot be empty.

The data is loaded immediately; external objects are loaded asynchronously.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.load`, :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.setHtml`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.toHtml`.
