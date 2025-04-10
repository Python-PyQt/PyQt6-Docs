.. sip:class-description::
    :status: todo
    :brief: Encapsulates the data of a WebAuth UX request
    :digest: 0765e349a63bb4d1ee2d972de3850c08

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest` class encapsulates the data of a WebAuth UX request.

This class contains the information and API for WebAuth UX. WebAuth may require user interaction during the authentication process. These requests are handled by displaying a dialog to users. `QtWebEngine <https://doc.qt.io/qt-6/qtwebengine-qmlmodule.html>`_ currently supports user verification, resident credentials, and display request failure UX requests.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest` models a WebAuth UX request throughout its life cycle, starting with showing a UX dialog, updating it's content through state changes, and finally closing the dialog.

WebAuth UX requests are normally triggered when the authenticator requires user interaction. It is the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage`'s responsibility to notify the application of the new WebAuth UX requests, which it does by emitting the webAuthUxRequested signal together with a newly created :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest`. The application can then examine this request and display a WebAuth UX dialog.

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest` object periodically emits the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.stateChanged` signal to notify potential observers of the current WebAuth UX states. The observers update the WebAuth dialog accordingly.

For more information about how to handle web engine authenticator requests, see the `Simple Browser <https://doc.qt.io/qt-6/qtwebengine-webenginewidgets-simplebrowser-example.html>`_.
