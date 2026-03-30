.. sip:method-description::
    :status: todo
    :pysig: 011fa8405e5b5ba15aadd278220a5d31
    :realsig: (const QString&) const
    :digest: cd114f2ccb147d6f2bfcbcd8ed061db7

Returns a :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`.

The returned request's URL is formed by appending the provided *path* to the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.baseUrl` (which may itself have a path component).

.. seealso:: createRequest(const QString &, const QUrlQuery &), :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.createRequest`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.baseUrl`.
