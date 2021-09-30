.. sip:method-description::
    :status: todo
    :pysig: 6278ade37c473d94eed7911fa2596831
    :realsig: (const QNetworkProxy&)
    :digest: 8ce37376a280a27873318f46fa1f7063

Sets the explicit network proxy for this server to *networkProxy*.

To disable the use of a proxy, use the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.NoProxy` proxy type:

::

    server->setProxy(QNetworkProxy::NoProxy);

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.proxy`.
