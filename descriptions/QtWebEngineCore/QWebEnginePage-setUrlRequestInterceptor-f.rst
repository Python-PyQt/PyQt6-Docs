.. sip:method-description::
    :status: todo
    :pysig: a5d2892193363daf038996a8c0eaa399
    :realsig: (QWebEngineUrlRequestInterceptor*)
    :digest: 3a250a0e82bd7521d9cda94d1267c1e1

Registers the request interceptor *interceptor* to intercept URL requests.

The page does not take ownership of the pointer. This interceptor is called after any interceptors on the profile, and unlike profile interceptors, only URL requests from this page are intercepted.

To unset the request interceptor, set a ``nullptr``.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInfo`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setUrlRequestInterceptor`.
