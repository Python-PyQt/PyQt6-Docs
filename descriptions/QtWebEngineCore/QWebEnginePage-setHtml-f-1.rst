.. sip:method-description::
    :status: todo
    :pysig: 3e8614e0affc4b6a6b7c16883bc643a6
    :realsig: (const QString&, const QUrl&)
    :digest: 214a94f9e9992f62e97e21aaee80f1f1

Sets the content of this page to *html*. *baseUrl* is optional and used to resolve relative URLs in the document, such as referenced images or stylesheets.

The *html* is loaded immediately; external objects are loaded asynchronously.

If a script in the *html* runs longer than the default script timeout (currently 10 seconds), for example due to being blocked by a modal JavaScript alert dialog, this method will return as soon as possible after the timeout and any subsequent *html* will be loaded asynchronously.

When using this method, the web engine assumes that external resources, such as JavaScript programs or style sheets, are encoded in UTF-8 unless otherwise specified. For example, the encoding of an external script can be specified through the charset attribute of the HTML script tag. It is also possible for the encoding to be specified by the web server.

This is a convenience function equivalent to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setContent`\ (html, "text/html", baseUrl).

**Note:** This method will not affect session or global history for the page.

**Warning:** This function works only for HTML, for other mime types (such as XHTML and SVG) :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setContent` should be used instead.

**Warning:** The content will be percent encoded before being sent to the renderer via IPC. This may increase its size. The maximum size of the percent encoded content is 2 megabytes minus 30 bytes.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.toHtml`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setContent`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.load`.
