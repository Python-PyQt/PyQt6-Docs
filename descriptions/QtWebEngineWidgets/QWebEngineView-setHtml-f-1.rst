.. sip:method-description::
    :status: todo
    :pysig: 3e8614e0affc4b6a6b7c16883bc643a6
    :realsig: (const QString&, const QUrl&)
    :digest: 7c2b71064d32e623963b4b2a01e2235c

Sets the content of the web view to the specified *html* content.

*baseUrl* is optional and used to resolve relative URLs in the document, such as referenced images or stylesheets. For example, if *html* is retrieved from ``http://www.example.com/documents/overview.html``, which is the base URL, then an image referenced with the relative URL, ``diagram.png``, should be at ``http://www.example.com/documents/diagram.png``.

The HTML document is loaded immediately, whereas external objects are loaded asynchronously.

When using this method, Qt WebEngine assumes that external resources, such as JavaScript programs or style sheets, are encoded in UTF-8 unless otherwise specified. For example, the encoding of an external script can be specified through the ``charset`` attribute of the HTML script tag. Alternatively, the encoding can be specified by the web server.

This is a convenience function equivalent to ``setContent(html, "text/html;charset=UTF-8", baseUrl)``.

**Warning:** This function works only for HTML. For other MIME types (such as XHTML or SVG), :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.setContent` should be used instead.

**Note:** Content larger than 2 MB cannot be displayed, because setHtml() converts the provided HTML to percent-encoding and places ``data``: in front of it to create the URL that it navigates to. Thereby, the provided code becomes a URL that exceeds the 2 MB limit set by Chromium. If the content is too large, the :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.loadFinished` signal is triggered with ``success=false``.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.load`, :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.setContent`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.toHtml`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setContent`.
