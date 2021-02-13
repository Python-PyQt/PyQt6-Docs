.. sip:method-description::
    :status: todo
    :pysig: 28113419a5d8ea3c7dc46a17904155df
    :realsig: (const QList<QNetworkCookie>&,const QUrl&)
    :digest: f5082429d3f32813bc0aad70062c49f6

Adds the cookies in the list *cookieList* to this cookie jar. Before being inserted cookies are normalized.

Returns ``true`` if one or more cookies are set for *url*, otherwise false.

If a cookie already exists in the cookie jar, it will be overridden by those in *cookieList*.

The default :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar` class implements only a very basic security policy (it makes sure that the cookies' domain and path match the reply's). To enhance the security policy with your own algorithms, override .

Also, :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar` does not have a maximum cookie jar size. Reimplement this function to discard older cookies to create room for new ones.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.cookiesForUrl`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setCookieJar`, :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.normalize`.
