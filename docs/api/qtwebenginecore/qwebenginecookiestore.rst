:orphan:

.. sip:class:: PyQt6.QtWebEngineCore.QWebEngineCookieStore
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWebEngineCore/QWebEngineCookieStore-c.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCookieStore.deleteAllCookies
        :description: QtWebEngineCore/QWebEngineCookieStore-deleteAllCookies-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCookieStore.deleteCookie
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`
            origin: :sip:ref:`~PyQt6.QtCore.QUrl` = QUrl()
        :description: QtWebEngineCore/QWebEngineCookieStore-deleteCookie-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCookieStore.deleteSessionCookies
        :description: QtWebEngineCore/QWebEngineCookieStore-deleteSessionCookies-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCookieStore.loadAllCookies
        :description: QtWebEngineCore/QWebEngineCookieStore-loadAllCookies-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCookieStore.setCookie
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`
            origin: :sip:ref:`~PyQt6.QtCore.QUrl` = QUrl()
        :description: QtWebEngineCore/QWebEngineCookieStore-setCookie-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCookieStore.setCookieFilter
        :args:
            filterCallback: Callable[[FilterRequest], bool] = 0
        :description: QtWebEngineCore/QWebEngineCookieStore-setCookieFilter-f.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineCookieStore.cookieAdded
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`
        :description: QtWebEngineCore/QWebEngineCookieStore-cookieAdded-s.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineCookieStore.cookieRemoved
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`
        :description: QtWebEngineCore/QWebEngineCookieStore-cookieRemoved-s.rst
