.. sip:method-description::
    :status: todo
    :pysig: 6a6478e67821a01a1c2eb359de8db236
    :realsig: (const QByteArray&)
    :digest: 44e03f10da8970aca386affc96a4980e

Parses the cookie string *cookieString* as received from a server response in the "Set-Cookie:" header. If there's a parsing error, this function returns an empty list.

Since the HTTP header can set more than one cookie at the same time, this function returns a QList<\ :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`>, one for each cookie that is parsed.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.toRawForm`.
