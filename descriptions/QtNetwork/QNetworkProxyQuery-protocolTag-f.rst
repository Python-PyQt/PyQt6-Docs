.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: cb61ffffe5ed290dda2922cf85696d95

Returns the protocol tag for this :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery` object, or an empty QString in case the protocol tag is unknown.

In the case of queries of type :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.UrlRequest`, this function returns the value of the scheme component of the URL.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.setProtocolTag`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.url`.
