.. sip:method-description::
    :status: todo
    :pysig: 28663408623c214f4263f0af774166a6
    :realsig: (const QUrl&,QWebEnginePage::NavigationType,bool)
    :digest: 2977043b99dcd39fe13526e81af22e96

This function is called upon receiving a request to navigate to the specified *url* by means of the specified navigation type *type*. *isMainFrame* indicates whether the request corresponds to the main frame or a child frame. If the function returns ``true``, the navigation request is accepted and ``url`` is loaded. The default implementation accepts all navigation requests.

Navigation requests can be delegated to the Qt application instead of having the HTML handler engine process them by overloading this function. This is necessary when an HTML document is used as part of the user interface, and not to display external data, for example, when displaying a list of results.

**Note:** This function is not called for fragment navigation on the same page. Such navigation, for example, happens by clicking a link to a '#fragment' within the page. It does not trigger a load to a different document, even though it changes page's url and adds history entry. It only serves as a shortcut to scroll within the page. Hence, no delegation of this navigation type is expected to happen.

**Note:** The loading process is started and the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.loadStarted` signal is emitted *before* the request is accepted or rejected. Therefore, a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.loadFinished` signal that returns ``false`` is to be expected even after delegating the request.

**Note:** When using :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setHtml` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setContent` with relative links, make sure to specify a base url, otherwise the links will be considered invalid and no navigation requests will be emitted.

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInterceptor` class offers further options for intercepting and manipulating requests.
