.. sip:class-description::
    :status: todo
    :brief: Network layer proxy
    :digest: 44082f702ba1dff0981d96067bfe5b44

The :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy` class provides a network layer proxy.

:sip:ref:`~PyQt6.QtNetwork.QNetworkProxy` provides the method for configuring network layer proxy support to the Qt network classes. The currently supported classes are :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`, :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`, :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`, :sip:ref:`~PyQt6.QtNetwork.QTcpServer` and :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`. The proxy support is designed to be as transparent as possible. This means that existing network-enabled applications that you have written should automatically support network proxy using the following code.

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qnetworkproxy.py
    :lines: 54-60

An alternative to setting an application wide proxy is to specify the proxy for individual sockets using :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setProxy` and :sip:ref:`~PyQt6.QtNetwork.QTcpServer.setProxy`. In this way, it is possible to disable the use of a proxy for specific sockets using the following code:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qnetworkproxy.py
    :lines: 65-65

Network proxy is not used if the address used in :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connectToHost`, bind() or :sip:ref:`~PyQt6.QtNetwork.QTcpServer.listen` is equivalent to :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.LocalHost` or :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.LocalHostIPv6`.

Each type of proxy support has certain restrictions associated with it. You should read the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.ProxyType` documentation carefully before selecting a proxy type to use.

**Note:** Changes made to currently connected sockets do not take effect. If you need to change a connected socket, you should reconnect it.

.. _qnetworkproxy-socks5:

SOCKS5
------

The SOCKS5 support since Qt 4 is based on `RFC 1928 <http://www.rfc-editor.org/rfc/rfc1928.txt>`_ and `RFC 1929 <http://www.rfc-editor.org/rfc/rfc1929.txt>`_. The supported authentication methods are no authentication and username/password authentication. Both IPv4 and IPv6 are supported. Domain names are resolved through the SOCKS5 server if the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.Capabilities.HostNameLookupCapability` is enabled, otherwise they are resolved locally and the IP address is sent to the server. There are several things to remember when using SOCKS5 with :sip:ref:`~PyQt6.QtNetwork.QUdpSocket` and :sip:ref:`~PyQt6.QtNetwork.QTcpServer`:

With :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`, a call to bind() may fail with a timeout error. If a port number other than 0 is passed to bind(), it is not guaranteed that it is the specified port that will be used. Use localPort() and localAddress() to get the actual address and port number in use. Because proxied UDP goes through two UDP connections, it is more likely that packets will be dropped.

With :sip:ref:`~PyQt6.QtNetwork.QTcpServer` a call to :sip:ref:`~PyQt6.QtNetwork.QTcpServer.listen` may fail with a timeout error. If a port number other than 0 is passed to :sip:ref:`~PyQt6.QtNetwork.QTcpServer.listen`, then it is not guaranteed that it is the specified port that will be used. Use :sip:ref:`~PyQt6.QtNetwork.QTcpServer.serverPort` and :sip:ref:`~PyQt6.QtNetwork.QTcpServer.serverAddress` to get the actual address and port used to listen for connections. SOCKS5 only supports one accepted connection per call to :sip:ref:`~PyQt6.QtNetwork.QTcpServer.listen`, and each call is likely to result in a different :sip:ref:`~PyQt6.QtNetwork.QTcpServer.serverPort` being used.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`, :sip:ref:`~PyQt6.QtNetwork.QTcpServer`.
