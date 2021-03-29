.. sip:class-description::
    :status: todo
    :brief: Used to query the proxy settings for a socket
    :digest: a57b99d7b90fcf57c6db742789d95b47

The :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery` class is used to query the proxy settings for a socket.

:sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery` holds the details of a socket being created or request being made. It is used by :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy` and :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory` to allow applications to have a more fine-grained control over which proxy servers are used, depending on the details of the query. This allows an application to apply different settings, according to the protocol or destination hostname, for instance.

:sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery` supports the following criteria for selecting the proxy:

* the type of query

* the local port number to use

* the destination host name

* the destination port number

* the protocol name, such as "http" or "ftp"

* the URL being requested

The destination host name is the host in the connection in the case of outgoing connection sockets. It is the ``hostName`` parameter passed to QTcpSocket::connectToHost() or the host component of a URL requested with :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`.

The destination port number is the requested port to connect to in the case of outgoing sockets, while the local port number is the port the socket wishes to use locally before attempting the external connection. In most cases, the local port number is used by listening sockets only (\ :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`) or by datagram sockets (\ :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`).

The protocol name is an arbitrary string that indicates the type of connection being attempted. For example, it can match the scheme of a URL, like "http", "https" and "ftp". In most cases, the proxy selection will not change depending on the protocol, but this information is provided in case a better choice can be made, like choosing an caching HTTP proxy for HTTP-based connections, but a more powerful SOCKSv5 proxy for all others.

Some of the criteria may not make sense in all of the types of query. The following table lists the criteria that are most commonly used, according to the type of query.

+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Query type                                                          | Description                                                                                                                                                                                                                                                                                                                                                                |
+=====================================================================+============================================================================================================================================================================================================================================================================================================================================================================+
| :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.TcpSocket`  | Normal sockets requesting a connection to a remote server, like :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`. The peer hostname and peer port match the values passed to QTcpSocket::connectToHost(). The local port is usually -1, indicating the socket has no preference in which port should be used. The URL component is not used.                                         |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.UdpSocket`  | Datagram-based sockets, which can both send and receive. The local port, remote host or remote port fields can all be used or be left unused, depending on the characteristics of the socket. The URL component is not used.                                                                                                                                               |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.SctpSocket` | Message-oriented sockets requesting a connection to a remote server. The peer hostname and peer port match the values passed to QSctpSocket::connectToHost(). The local port is usually -1, indicating the socket has no preference in which port should be used. The URL component is not used.                                                                           |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.TcpServer`  | Passive server sockets that listen on a port and await incoming connections from the network. Normally, only the local port is used, but the remote address could be used in specific circumstances, for example to indicate which remote host a connection is expected from. The URL component is not used.                                                               |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.UrlRequest` | A more high-level request, such as those coming from :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`. These requests will inevitably use an outgoing TCP socket, but the this query type is provided to indicate that more detailed information is present in the URL component. For ease of implementation, the URL's host and port are set as the destination address. |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyQuery.QueryType.SctpServer` | Passive server sockets that listen on an SCTP port and await incoming connections from the network. Normally, only the local port is used, but the remote address could be used in specific circumstances, for example to indicate which remote host a connection is expected from. The URL component is not used.                                                         |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

It should be noted that any of the criteria may be missing or unknown (an empty QString for the hostname or protocol name, -1 for the port numbers). If that happens, the functions executing the query should make their best guess or apply some implementation-defined default values.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setProxy`.
