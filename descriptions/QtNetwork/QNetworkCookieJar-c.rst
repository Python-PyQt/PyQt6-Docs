.. sip:class-description::
    :status: todo
    :brief: Implements a simple jar of QNetworkCookie objects
    :digest: 859d7548b8e0de4b8779973e596f6c49

The :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar` class implements a simple jar of :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie` objects.

Cookies are small bits of information that stateless protocols like HTTP use to maintain some persistent information across requests.

A cookie is set by a remote server when it replies to a request and it expects the same cookie to be sent back when further requests are sent.

The cookie jar is the object that holds all cookies set in previous requests. Web browsers save their cookie jars to disk in order to conserve permanent cookies across invocations of the application.

:sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar` does not implement permanent storage: it only keeps the cookies in memory. Once the :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar` object is deleted, all cookies it held will be discarded as well. If you want to save the cookies, you should derive from this class and implement the saving to disk to your own storage format.

This class implements only the basic security recommended by the cookie specifications and does not implement any cookie acceptance policy (it accepts all cookies set by any requests). In order to override those rules, you should reimplement the :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.cookiesForUrl` and :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.setCookiesFromUrl` virtual functions. They are called by :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` and :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` when they detect new cookies and when they require cookies.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setCookieJar`.
