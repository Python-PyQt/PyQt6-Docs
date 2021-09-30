.. sip:class-description::
    :status: todo
    :brief: Access to Chromium's cookies
    :digest: c088856f593ae75497d84c046ab92d40

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineCookieStore` class provides access to Chromium's cookies.

The class allows to access HTTP cookies of Chromium for a specific profile. It can be used to synchronize cookies of Chromium and the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`, as well as to set, delete, and intercept cookies during navigation. Because cookie operations are asynchronous, the user can choose to provide a callback function to get notified about the success of the operation. The signal handlers for removal and addition should not be used to execute heavy tasks, because they might block the IO thread in case of a blocking connection.

Use :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.cookieStore` and :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.cookieStore` to access the cookie store object for a specific profile.
