.. sip:class-description::
    :status: todo
    :brief: Information about URL requests
    :digest: 773a8d5108889f87530f26be6f778927

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInfo` class provides information about URL requests.

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInfo` is useful for setting extra header fields for requests or for redirecting certain requests without payload data to another URL. This class cannot be instantiated or copied by the user, instead it will be created by Qt WebEngine and sent through the virtual function :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInterceptor.interceptRequest` if an interceptor has been set.
