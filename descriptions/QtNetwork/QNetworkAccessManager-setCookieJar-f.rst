.. sip:method-description::
    :status: todo
    :pysig: dca31ae5506785bc4f78ca881e9cb989
    :realsig: (QNetworkCookieJar*)
    :digest: 9c09c4646caff259d85c687ba25eb14c

Sets the manager's cookie jar to be the *cookieJar* specified. The cookie jar is used by all requests dispatched by the manager.

Use this function to set the cookie jar object to a class that implements additional features, like saving the cookies to permanent storage.

**Note:** :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` takes ownership of the *cookieJar* object.

If *cookieJar* is in the same thread as this :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`, it will set the parent of the *cookieJar* so that the cookie jar is deleted when this object is deleted as well. If you want to share cookie jars between different :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` objects, you may want to set the cookie jar's parent to 0 after calling this function.

:sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` by default does not implement any cookie policy of its own: it accepts all cookies sent by the server, as long as they are well formed and meet the minimum security requirements (cookie domain matches the request's and cookie path matches the request's). In order to implement your own security policy, override the :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.cookiesForUrl` and :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.setCookiesFromUrl` virtual functions. Those functions are called by :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` when it detects a new cookie.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.cookieJar`, :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.cookiesForUrl`, :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.setCookiesFromUrl`.
