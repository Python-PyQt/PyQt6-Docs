.. sip:method-description::
    :status: todo
    :pysig: 6278ade37c473d94eed7911fa2596831
    :realsig: (const QNetworkProxy&)
    :digest: 2797298ddadd968d707230ab69770b6c

Sets the explicit network proxy for this socket to *networkProxy*.

To disable the use of a proxy for this socket, use the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.NoProxy` proxy type:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_socket_qtcpserver.py
    :lines: 54-54

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QTcpServer.proxy`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`.
