.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 158dc2837faa96243932d2fa586083a1

Returns the port number for the outgoing request or -1 if the port number is not known.

If the query type is :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.UrlRequest`, this function returns the port number of the URL being requested. In general, frameworks will fill in the port number from their default values.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.peerHostName`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.localPort`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.setPeerPort`.
