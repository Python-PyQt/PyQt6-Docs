.. sip:class-description::
    :status: todo
    :brief: Fine-grained proxy selection
    :digest: fa14d85fbe8d556e2eda869e3378c494

The :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory` class provides fine-grained proxy selection.

:sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory` is an extension to :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`, allowing applications to have a more fine-grained control over which proxy servers are used, depending on the socket requesting the proxy. This allows an application to apply different settings, according to the protocol or destination hostname, for instance.

:sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory` can be set globally for an application, in which case it will override any global proxies set with :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setApplicationProxy`. If set globally, any sockets created with Qt will query the factory to determine the proxy to be used.

A factory can also be set in certain frameworks that support multiple connections, such as :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`. When set on such object, the factory will be queried for sockets created by that framework only.

.. _qnetworkproxyfactory-system-proxies:

System Proxies
--------------

You can configure a factory to use the system proxy's settings. Call the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration` function with true to enable this behavior, or false to disable it.

Similarly, you can use a factory to make queries directly to the system proxy by calling its :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory.systemProxyForQuery` function.

**Warning:** Depending on the configuration of the user's system, the use of system proxy features on certain platforms may be subject to limitations. The :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory.systemProxyForQuery` documentation contains a list of these limitations for those platforms that are affected.
