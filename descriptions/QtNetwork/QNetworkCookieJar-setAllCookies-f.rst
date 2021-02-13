.. sip:method-description::
    :status: todo
    :pysig: f7da654c5304d5a5d0ed45ce18c29629
    :realsig: (const QList<QNetworkCookie>&)
    :digest: 77fbb41f70f489ae6e33c710811a7836

Sets the internal list of cookies held by this cookie jar to be *cookieList*. This function is suitable for derived classes to implement loading cookies from permanent storage, or their own cookie acceptance policies by reimplementing :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.setCookiesFromUrl`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.allCookies`, :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.setCookiesFromUrl`.
