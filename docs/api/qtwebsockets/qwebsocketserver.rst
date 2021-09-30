:orphan:

.. sip:class:: PyQt6.QtWebSockets.QWebSocketServer
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWebSockets/QWebSocketServer-c.rst

    .. sip:enum:: PyQt6.QtWebSockets.QWebSocketServer.SslMode
        :description: QtWebSockets/QWebSocketServer-SslMode-e.rst

        .. sip:enum-member:: PyQt6.QtWebSockets.QWebSocketServer.SslMode.NonSecureMode
            :description: QtWebSockets/QWebSocketServer-SslMode-NonSecureMode-v.rst

        .. sip:enum-member:: PyQt6.QtWebSockets.QWebSocketServer.SslMode.SecureMode
            :description: QtWebSockets/QWebSocketServer-SslMode-SecureMode-v.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.__init__
        :args:
            str
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.SslMode`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWebSockets/QWebSocketServer-__init__-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.close
        :description: QtWebSockets/QWebSocketServer-close-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.error
        :returns:
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.CloseCode`
        :description: QtWebSockets/QWebSocketServer-error-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.errorString
        :returns:
            str
        :description: QtWebSockets/QWebSocketServer-errorString-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.handleConnection
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`
        :description: QtWebSockets/QWebSocketServer-handleConnection-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.handshakeTimeoutMS
        :returns:
            int
        :description: QtWebSockets/QWebSocketServer-handshakeTimeoutMS-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.hasPendingConnections
        :returns:
            bool
        :description: QtWebSockets/QWebSocketServer-hasPendingConnections-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.isListening
        :returns:
            bool
        :description: QtWebSockets/QWebSocketServer-isListening-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.listen
        :args:
            address: Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`] = :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.Any`
            port: int = 0
        :returns:
            bool
        :description: QtWebSockets/QWebSocketServer-listen-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.maxPendingConnections
        :returns:
            int
        :description: QtWebSockets/QWebSocketServer-maxPendingConnections-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.nextPendingConnection
        :returns:
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocket`
        :description: QtWebSockets/QWebSocketServer-nextPendingConnection-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.pauseAccepting
        :description: QtWebSockets/QWebSocketServer-pauseAccepting-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.proxy
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtWebSockets/QWebSocketServer-proxy-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.resumeAccepting
        :description: QtWebSockets/QWebSocketServer-resumeAccepting-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.secureMode
        :returns:
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.SslMode`
        :description: QtWebSockets/QWebSocketServer-secureMode-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.serverAddress
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtWebSockets/QWebSocketServer-serverAddress-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.serverName
        :returns:
            str
        :description: QtWebSockets/QWebSocketServer-serverName-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.serverPort
        :returns:
            int
        :description: QtWebSockets/QWebSocketServer-serverPort-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.serverUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebSockets/QWebSocketServer-serverUrl-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.setHandshakeTimeout
        :args:
            int
        :description: QtWebSockets/QWebSocketServer-setHandshakeTimeout-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.setMaxPendingConnections
        :args:
            int
        :description: QtWebSockets/QWebSocketServer-setMaxPendingConnections-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.setProxy
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtWebSockets/QWebSocketServer-setProxy-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.setServerName
        :args:
            str
        :description: QtWebSockets/QWebSocketServer-setServerName-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.setSocketDescriptor
        :args:
            PyQt6.sip.voidptr
        :returns:
            bool
        :description: QtWebSockets/QWebSocketServer-setSocketDescriptor-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.setSslConfiguration
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtWebSockets/QWebSocketServer-setSslConfiguration-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.socketDescriptor
        :returns:
            PyQt6.sip.voidptr
        :description: QtWebSockets/QWebSocketServer-socketDescriptor-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.sslConfiguration
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtWebSockets/QWebSocketServer-sslConfiguration-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocketServer.supportedVersions
        :returns:
            List[:sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.Version`]
        :description: QtWebSockets/QWebSocketServer-supportedVersions-f.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocketServer.acceptError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtWebSockets/QWebSocketServer-acceptError-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocketServer.closed
        :description: QtWebSockets/QWebSocketServer-closed-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocketServer.newConnection
        :description: QtWebSockets/QWebSocketServer-newConnection-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocketServer.originAuthenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocketCorsAuthenticator`
        :description: QtWebSockets/QWebSocketServer-originAuthenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocketServer.peerVerifyError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslError`
        :description: QtWebSockets/QWebSocketServer-peerVerifyError-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocketServer.preSharedKeyAuthenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator`
        :description: QtWebSockets/QWebSocketServer-preSharedKeyAuthenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocketServer.serverError
        :args:
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.CloseCode`
        :description: QtWebSockets/QWebSocketServer-serverError-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocketServer.sslErrors
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslError`]
        :description: QtWebSockets/QWebSocketServer-sslErrors-s.rst
