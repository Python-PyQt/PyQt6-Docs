.. sip:method-description::
    :status: todo
    :pysig: 6278ade37c473d94eed7911fa2596831
    :realsig: (const QNetworkProxy&)
    :digest: 99e9e37dcb6be4f1305f5696086b5a20

Sets the explicit network proxy for this socket to *networkProxy*.

To disable the use of a proxy for this socket, use the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.NoProxy` proxy type:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_socket_qabstractsocket.py
    :lines: 70-70

The default value for the proxy is :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.DefaultProxy`, which means the socket will use the application settings: if a proxy is set with :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setApplicationProxy`, it will use that; otherwise, if a factory is set with :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory.setApplicationProxyFactory`, it will query that factory with type :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.TcpSocket`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.proxy`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory.queryProxy`.
