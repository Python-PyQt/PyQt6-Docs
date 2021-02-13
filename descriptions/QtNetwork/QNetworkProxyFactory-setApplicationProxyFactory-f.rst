.. sip:method-description::
    :status: todo
    :pysig: 5a12b780ee1e540fd7652ba2355831a0
    :realsig: (QNetworkProxyFactory*)
    :digest: 1cd8779cb3aba10096b0d05048dbb0d3

Sets the application-wide proxy factory to be *factory*. This function will take ownership of that object and will delete it when necessary.

The application-wide proxy is used as a last-resort when all other proxy selection requests returned :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.DefaultProxy`. For example, :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` objects can have a proxy set with QTcpSocket::setProxy, but if none is set, the proxy factory class set with this function will be queried.

If you set a proxy factory with this function, any application level proxies set with :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setApplicationProxy` will be overridden, and :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory.usesSystemConfiguration` will return ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setApplicationProxy`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.proxy`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setProxy`.
