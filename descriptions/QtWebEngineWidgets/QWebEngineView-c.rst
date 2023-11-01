.. sip:class-description::
    :status: todo
    :brief: Widget that is used to view and edit web documents
    :digest: a6f6fd4fab4e29513df320bcfcf93043

The :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView` class provides a widget that is used to view and edit web documents.

A *web view* is the main widget component of the Qt WebEngine web browsing module. It can be used in various applications to display web content live from the Internet.

A *web site* can be loaded to a web view with the :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.load` function. The GET method is always used to load URLs.

Like all Qt widgets, the show() function must be invoked in order to display the web view. The snippet below illustrates this:

.. literalinclude:: ../../../snippets/qtwebengine-src-webenginewidgets-doc-snippets-simple-main.py
    :lines: 62-64

Alternatively, :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.setUrl` can be used to load a web site. If you have the HTML content readily available, you can use :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.setHtml` instead.

The :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.loadStarted` signal is emitted when the view begins loading and the :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.loadProgress` signal is emitted whenever an element of the web view completes loading, such as an embedded image or a script. The :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.loadFinished` signal is emitted when the view has been loaded completely. Its argument, either ``true`` or ``false``, indicates whether loading was successful or failed.

The :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.page` function returns a pointer to a *web page* object. A :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView` contains a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage`, which in turn allows access to the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory` in the page's context.

The title of an HTML document can be accessed with the :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.title` property. Additionally, a web site may specify an icon, which can be accessed using the :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.icon` or its URL using the :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.iconUrl` property. If the title or the icon changes, the corresponding :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.titleChanged`, :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.iconChanged` and :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.iconUrlChanged` signals will be emitted. The :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.zoomFactor` property enables zooming the contents of the web page by a scale factor.

The widget features a context menu that is tailored to the element at hand, and includes actions useful in a browser. For a custom context menu, or for embedding actions in a menu or toolbar, the individual actions are available via :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.pageAction`. The web view maintains the state of the returned actions, but allows modification of action properties such as :sip:ref:`~PyQt6.QtGui.QAction.text` or :sip:ref:`~PyQt6.QtGui.QAction.icon`. The action semantics can also be triggered directly through :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.triggerPageAction`.

If you want to provide support for web sites that allow the user to open new windows, such as pop-up windows, you can subclass :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView` and reimplement the :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.createWindow` function.

.. seealso:: `WebEngine Widgets Simple Browser Example <https://doc.qt.io/qt-6/qtwebengine-webenginewidgets-simplebrowser-example.html>`_, `WebEngine Content Manipulation Example <https://doc.qt.io/qt-6/qtwebengine-webenginewidgets-contentmanipulation-example.html>`_.
