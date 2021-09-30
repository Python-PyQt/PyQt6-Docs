.. sip:class-description::
    :status: todo
    :brief: Enables accepting or rejecting requests for entering and exiting the fullscreen mode
    :digest: b5a2fc683c8fb55401bc60aa4fcc6a47

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFullScreenRequest` class enables accepting or rejecting requests for entering and exiting the fullscreen mode.

To allow elements such as videos to be shown in the fullscreen mode, applications must set :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineSettings.WebAttribute.FullScreenSupportEnabled` and connect to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.fullScreenRequested`, which takes a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFullScreenRequest` instance as an argument.

If an element of a web page requests to be shown in the fullscreen mode, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.fullScreenRequested` will be emitted with an :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFullScreenRequest` instance as an argument where :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFullScreenRequest.toggleOn` returns ``true``. The signal handler needs to then either call :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFullScreenRequest.accept` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFullScreenRequest.reject`.

If the request to enter the fullscreen mode is accepted, the element requesting fullscreen mode will fill the viewport, but it is up to the application to make the view fullscreen or to move the page to a view that is in the fullscreen mode.

Likewise, a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.fullScreenRequested` will be emitted when the user wants to leave the full screen mode (that is, through the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.WebAction.ExitFullScreen` context menu action). In this case, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFullScreenRequest.toggleOn` will return ``false``, and the signal handler again needs to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFullScreenRequest.accept` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFullScreenRequest.reject` the request. If it is accepted, the applicaton needs to make sure that the global window state is restored.
