.. sip:method-description::
    :status: todo
    :pysig: e27e396ef2aa2252acd08b3fe2e2bb39
    :realsig: (const QUrl&) const
    :digest: 3dce71cf498abed4d947500b6225fb7b

Returns the cookies to be added to when a request is sent to *url*. This function is called by the default :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.createRequest`, which adds the cookies returned by this function to the request being sent.

If more than one cookie with the same name is found, but with differing paths, the one with longer path is returned before the one with shorter path. In other words, this function returns cookies sorted decreasingly by path length.

The default :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar` class implements only a very basic security policy (it makes sure that the cookies' domain and path match the reply's). To enhance the security policy with your own algorithms, override .

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.setCookiesFromUrl`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setCookieJar`.
