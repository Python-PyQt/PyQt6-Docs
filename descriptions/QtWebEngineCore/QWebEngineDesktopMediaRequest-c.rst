.. sip:class-description::
    :status: todo
    :brief: A request for populating a dialog with available sources for screen capturing
    :digest: 5687410fc46e49c58032a56a10255345

A request for populating a dialog with available sources for screen capturing.

To allow web applications to capture contents of a display, applications must connect to QWebEnginePage::desktopMediaRequested, which takes a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDesktopMediaRequest` instance as an argument.

If a web application requests access to the contents of a display, QWebEnginePage::desktopMediaRequested will be emitted with a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDesktopMediaRequest` instance as an argument which holds references to QAbstractListModels for available windows and screens that can be captured.

The data model's *Qt::DisplayRole* specifies the name of the source which is the title of a window or the number of the display. The model is dynamically updated if the available list of sources has changed; e.g when a window is opened/closed.

The signal handler needs to then either call :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDesktopMediaRequest.selectScreen` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDesktopMediaRequest.selectWindow` to accept the request and start screensharing.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.desktopMediaRequested`.
