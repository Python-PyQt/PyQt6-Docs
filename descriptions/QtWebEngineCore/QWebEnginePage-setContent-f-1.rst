.. sip:method-description::
    :status: todo
    :pysig: 5a07c208d7353161fa982c612c26691c
    :realsig: (const QByteArray&, const QString&, const QUrl&)
    :digest: 3110b74a5320d25e0ffe0534e98a565b

Sets the content of the web page to *data*. If the *mimeType* argument is empty, it is assumed that the content is ``text/plain,charset=US-ASCII``.

External objects referenced in the content are located relative to *baseUrl*. For external objects with relative URLs to be loaded, ``baseUrl`` cannot be empty.

The *data* is loaded immediately; external objects are loaded asynchronously.

**Note:** This method will not affect session or global history for the page.

**Warning:** The content will be percent encoded before being sent to the renderer via IPC. This may increase its size. The maximum size of the percent encoded content is 2 megabytes minus 6 bytes plus the length of the mime type string.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.toHtml`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setHtml`.
