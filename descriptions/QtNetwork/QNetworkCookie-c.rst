.. sip:class-description::
    :status: todo
    :brief: Holds one network cookie
    :digest: 54fa4ddd1ec4a2a030e0daa8ebf6bdcc

The :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie` class holds one network cookie.

Cookies are small bits of information that stateless protocols like HTTP use to maintain some persistent information across requests.

A cookie is set by a remote server when it replies to a request and it expects the same cookie to be sent back when further requests are sent.

:sip:ref:`~PyQt6.QtNetwork.QNetworkCookie` holds one such cookie as received from the network. A cookie has a name and a value, but those are opaque to the application (that is, the information stored in them has no meaning to the application). A cookie has an associated path name and domain, which indicate when the cookie should be sent again to the server.

A cookie can also have an expiration date, indicating its validity. If the expiration date is not present, the cookie is considered a "session cookie" and should be discarded when the application exits (or when its concept of session is over).

:sip:ref:`~PyQt6.QtNetwork.QNetworkCookie` provides a way of parsing a cookie from the HTTP header format using the :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.parseCookies` function. However, when received in a :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`, the cookie is already parsed.

This class implements cookies as described by the initial cookie specification by Netscape, which is somewhat similar to the `RFC 2109 <http://www.rfc-editor.org/rfc/rfc2109.txt>`_ specification, plus the "HttpOnly" extension. The more recent `RFC 2965 <http://www.rfc-editor.org/rfc/rfc2965.txt>`_ specification (which uses the Set-Cookie2 header) is not supported.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`.
