.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 54b65b969b4eb151b657865296b244a6

This signal is emitted when the page finishes loading content. This signal is independent of script execution or page rendering. *ok* will indicate whether the load was successful or any error occurred.

**Note:** Navigation requests can be delegated to the Qt application instead of having the HTML handler engine process them by overloading the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.acceptNavigationRequest` function. Because the loading process is started and the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.loadStarted` signal is emitted *before* the request is accepted or rejected, a ``loadFinished()`` signal that returns ``false`` is to be expected even after delegating the request.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.loadStarted`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.acceptNavigationRequest`.
