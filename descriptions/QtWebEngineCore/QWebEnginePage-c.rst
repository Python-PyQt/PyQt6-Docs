.. sip:class-description::
    :status: todo
    :brief: Object to view and edit web documents
    :digest: cb7c05125e0d7b65f4155eda6fbfc31e

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` class provides an object to view and edit web documents.

A *web engine page* holds the contents of an HTML document, the history of navigated links, and actions.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage`'s API is very similar to QWebEngineView, as you are still provided with common functions like action() (known as pageAction() in QWebEngineView), triggerAction(), and findText().

A page can be loaded using load() or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setUrl`. Alternatively, if you have the HTML content readily available, you can use setHtml(). The GET method is always used to load URLs.

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` class also offers methods to retrieve both the URL currently loaded by the page (see :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.url`) as well as the URL originally requested to be loaded (see :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.requestedUrl`). These methods make possible the retrieval of the URL before and after a DNS resolution or a redirection occurs during the load process. The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.requestedUrl` also matches to the URL added to the page history (QWebEngineHistory) if load is successful.

The title of an HTML page can be accessed with the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.title` property. Additionally, a page may also specify an icon, which can be accessed using the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.icon` or its URL using the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.iconUrl` property. If the title or the icon changes, the corresponding :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.titleChanged`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.iconChanged` and :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.iconUrlChanged` signals will be emitted. The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.zoomFactor` property enables zooming the contents of the web page by a scale factor.

The loadStarted() signal is emitted when the page begins to load, whereas the loadProgress() signal is emitted whenever an element of the web page completes loading, such as an embedded image or a script. The loadFinished() signal is emitted when the page contents have been loaded completely, independent of script execution or page rendering. Its argument, either ``true`` or ``false``, indicates whether or not the load operation succeeded.

An HTML document is loaded in a *main frame* within the web page. If it references *child frames* (as defined by the ``<frame>`` or ``<iframe>`` elements), they are considered part of the content. Child frames are individually accessible only through JavaScript.

Web sites define *security origin* for safely accessing each other's resources for client-side scripting or databases. An origin consist of a host name, a scheme, and a port number. For example, the sites ``http://www.example.com/my/page.html`` and ``http://www.example.com/my/overview.html`` are allowed to share the same database or access each other's documents when used in HTML frame sets and JavaScript. At the same time, ``http://www.malicious.com/evil.html`` is prevented from accessing the resources of ``http://www.example.com/``, because they are of a different security origin. By default, local schemes like ``file://`` and ``qrc://`` are considered to be in the same security origin, and can access each other's resources. Local resources are by default restricted from accessing remote content, which means that ``file://`` will not be able to access ``http://domain.com/foo.html``.

Scripts can be executed on the web page by using runJavaScript(), either in the main JavaScript *world*, along with the rest of the JavaScript coming from the web contents, or in their own isolated world. While the DOM of the page can be accessed from any world, JavaScript variables of a function defined in one world are not accessible from a different one. :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScript.ScriptWorldId` provides some predefined IDs for this purpose. Using the ``runJavaScript()`` version without the world ID is the same as running the script in the ``MainWorld``.

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineSettings.WebAttribute.FocusOnNavigationEnabled` setting can be used to make the view associated with the page automatically receive focus when a navigation operation occurs (like loading or reloading a page or navigating through history).
