.. sip:class-description::
    :status: todo
    :brief: Abstract base class for URL interception
    :digest: aed049259f3bc07b5b8d412ceba9983f

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInterceptor` class provides an abstract base class for URL interception.

Implementing the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInterceptor` interface and installing the interceptor on the profile enables intercepting, blocking, and modifying URL requests before they reach the networking stack of Chromium.

You can install the interceptor on a profile via :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setUrlRequestInterceptor` or :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setUrlRequestInterceptor`.

When using the `Qt WebEngine Widgets Module <https://doc.qt.io/qt-6/qtwebengine-overview.html#qt-webengine-widgets-module>`_, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.acceptNavigationRequest` offers further options to accept or block requests.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInterceptor.interceptRequest`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInfo`.
