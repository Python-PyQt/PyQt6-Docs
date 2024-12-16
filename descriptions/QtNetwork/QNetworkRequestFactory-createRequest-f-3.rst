.. sip:method-description::
    :status: todo
    :pysig: ae8a1c8b222c68071f6b9190502f9941
    :realsig: (const QString&, const QUrlQuery&) const
    :digest: 549f257ed175dff15c641b56e82ca598

Returns a :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`.

The returned requests URL is formed by appending the provided *path* and *query* to the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.baseUrl` (which may have a path component).

If the provided *path* contains query items, they will be combined with the items in *query*.

.. seealso:: createRequest(const QUrlQuery&), :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.createRequest`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory.baseUrl`.
