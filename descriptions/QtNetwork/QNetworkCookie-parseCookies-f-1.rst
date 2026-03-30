.. sip:method-description::
    :status: todo
    :pysig: 9adfe90e815aa3cba50c70004acbdd46
    :realsig: (QByteArrayView)
    :digest: fe14fb82bdd1b2a389d6b95ee96e23bc

Parses the cookie string *cookieString* as received from a server response in the "Set-Cookie:" header. If there's a parsing error, this function returns an empty list.

Since the HTTP header can set more than one cookie at the same time, this function returns a QList<\ :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`>, one for each cookie that is parsed.

**Note:** In Qt versions prior to 6.7, this function took :sip:ref:`~PyQt6.QtCore.QByteArray` only.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.toRawForm`.
