.. sip:method-description::
    :status: todo
    :pysig: 07dad7f2b31a1d8e8d55d42c3135c19c
    :realsig: (QNetworkAccessManager::Operation,const QNetworkRequest&,QIODevice*)
    :digest: c62fe5c52f477be597aeef5938cdabb7

Returns a new :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` object to handle the operation *op* and request *originalReq*. The device *outgoingData* is always 0 for Get and Head requests, but is the value passed to :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post` and :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.put` in those operations (the :sip:ref:`~PyQt6.QtCore.QByteArray` variants will pass a :sip:ref:`~PyQt6.QtCore.QBuffer` object).

The default implementation calls :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar.cookiesForUrl` on the cookie jar set with :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setCookieJar` to obtain the cookies to be sent to the remote server.

The returned object must be in an open state.
