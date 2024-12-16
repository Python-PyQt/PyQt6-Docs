.. sip:method-description::
    :status: todo
    :pysig: e77dd7b9332b431b51a8eeeeee7021f7
    :realsig: () const
    :digest: 3c924a07d69c60a22dde4a16439c5d8f

Returns headers that are set in this network request.

If the proxy is not of type :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.HttpProxy` or :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.HttpCachingProxy`, default constructed :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setHeaders`.
