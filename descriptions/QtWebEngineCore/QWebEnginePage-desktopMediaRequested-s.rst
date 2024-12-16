.. sip:signal-description::
    :status: todo
    :pysig: 290eed9466d4ea31e169c6d985de1064
    :realsig: (const QWebEngineDesktopMediaRequest&)
    :digest: f6e2f8f93733f174063962c65785415a

This signal is emitted when a web application requests access to the contents of a display.

The *request* argument holds references to data models for windows and screens available for capturing. To accept the request, the signal handler can call either :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDesktopMediaRequest.selectScreen` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDesktopMediaRequest.selectWindow`.
