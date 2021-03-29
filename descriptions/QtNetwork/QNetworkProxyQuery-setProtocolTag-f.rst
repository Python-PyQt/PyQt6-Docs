.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 7378b74df508d77795288b860bf507d6

Sets the protocol tag for this :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery` object to be *protocolTag*.

The protocol tag is an arbitrary string that indicates which protocol is being talked over the socket, such as "http", "xmpp", "telnet", etc. The protocol tag is used by the backend to return a request that is more specific to the protocol in question: for example, a HTTP connection could be use a caching HTTP proxy server, while all other connections use a more powerful SOCKSv5 proxy server.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.protocolTag`.
