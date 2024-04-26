.. sip:method-description::
    :status: todo
    :pysig: a5d2892193363daf038996a8c0eaa399
    :realsig: (QWebEngineUrlRequestInterceptor*)
    :digest: b58e20172a2b2c021eefbf392da72ec6

Registers the request interceptor *interceptor* to intercept URL requests.

The page does not take ownership of the pointer. This interceptor is called after any interceptors on the profile, and unlike profile interceptors, only URL requests from this page are intercepted. If the original request was already blocked or redirected by the profile interceptor, it will not be intercepted by this.

To unset the request interceptor, set a ``nullptr``.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInfo`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setUrlRequestInterceptor`.
