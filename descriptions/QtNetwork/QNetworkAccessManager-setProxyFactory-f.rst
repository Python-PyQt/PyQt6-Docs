.. sip:method-description::
    :status: todo
    :pysig: e9048751f590d4c7444310b4fca7740f
    :realsig: (QNetworkProxyFactory*)
    :digest: 9c1fb3583ad8f67bac7b51b1a9f01e22

Sets the proxy factory for this class to be *factory*. A proxy factory is used to determine a more specific list of proxies to be used for a given request, instead of trying to use the same proxy value for all requests.

All queries sent by :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will have type :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.UrlRequest`.

For example, a proxy factory could apply the following rules:

* if the target address is in the local network (for example, if the hostname contains no dots or if it's an IP address in the organization's range), return :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.NoProxy`

* if the request is FTP, return an FTP proxy

* if the request is HTTP or HTTPS, then return an HTTP proxy

* otherwise, return a SOCKSv5 proxy server

The lifetime of the object *factory* will be managed by :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`. It will delete the object when necessary.

**Note:** If a specific proxy is set with :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setProxy`, the factory will not be used.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.proxyFactory`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setProxy`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery`.
