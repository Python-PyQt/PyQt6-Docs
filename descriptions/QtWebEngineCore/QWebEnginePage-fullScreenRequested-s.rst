.. sip:signal-description::
    :status: todo
    :pysig: 219b0048fb1c3f487245fe61d1cc3e20
    :realsig: (QWebEngineFullScreenRequest)
    :digest: c48363b59dff6740dcc346ae1f3273cc

This signal is emitted when the web page issues the request to enter fullscreen mode for a web-element, usually a video element.

The request object *fullScreenRequest* can be used to accept or reject the request.

If the request is accepted the element requesting fullscreen will fill the viewport, but it is up to the application to make the view fullscreen or move the page to a view that is fullscreen.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineSettings.WebAttribute.FullScreenSupportEnabled`.
