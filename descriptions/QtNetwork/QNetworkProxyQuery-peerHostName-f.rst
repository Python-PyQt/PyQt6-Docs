.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 4846f519560c258eb907c33f852b6fd0

Returns the host name or IP address being of the outgoing connection being requested, or an empty string if the remote hostname is not known.

If the query type is :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.UrlRequest`, this function returns the host component of the URL being requested.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.peerPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.localPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.setPeerHostName`.
