:orphan:

.. sip:class:: PyQt6.QtWebSockets.QWebSocket
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWebSockets/QWebSocket-c.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.__init__
        :args:
            origin: Optional[str] = ''
            version: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.Version` = :sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.Version.VersionLatest`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWebSockets/QWebSocket-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.abort
        :description: QtWebSockets/QWebSocket-abort-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.bytesToWrite
        :returns:
            int
        :description: QtWebSockets/QWebSocket-bytesToWrite-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.close
        :args:
            closeCode: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.CloseCode` = :sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeNormal`
            reason: Optional[str] = ''
        :description: QtWebSockets/QWebSocket-close-f-1.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.closeCode
        :returns:
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.CloseCode`
        :description: QtWebSockets/QWebSocket-closeCode-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.closeReason
        :returns:
            str
        :description: QtWebSockets/QWebSocket-closeReason-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.continueInterruptedHandshake
        :description: QtWebSockets/QWebSocket-continueInterruptedHandshake-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.error
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtWebSockets/QWebSocket-error-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.errorString
        :returns:
            str
        :description: QtWebSockets/QWebSocket-errorString-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.flush
        :returns:
            bool
        :description: QtWebSockets/QWebSocket-flush-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.handshakeOptions
        :returns:
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocketHandshakeOptions`
        :description: QtWebSockets/QWebSocket-handshakeOptions-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.ignoreSslErrors
        :description: QtWebSockets/QWebSocket-ignoreSslErrors-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.ignoreSslErrors
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslError`]
        :description: QtWebSockets/QWebSocket-ignoreSslErrors-f-1.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.isValid
        :returns:
            bool
        :description: QtWebSockets/QWebSocket-isValid-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.localAddress
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtWebSockets/QWebSocket-localAddress-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.localPort
        :returns:
            int
        :description: QtWebSockets/QWebSocket-localPort-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.maskGenerator
        :returns:
            :sip:ref:`~PyQt6.QtWebSockets.QMaskGenerator`
        :description: QtWebSockets/QWebSocket-maskGenerator-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.maxAllowedIncomingFrameSize
        :returns:
            int
        :description: QtWebSockets/QWebSocket-maxAllowedIncomingFrameSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.maxAllowedIncomingMessageSize
        :returns:
            int
        :description: QtWebSockets/QWebSocket-maxAllowedIncomingMessageSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.maxIncomingFrameSize
        :returns:
            int
        :static:
        :description: QtWebSockets/QWebSocket-maxIncomingFrameSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.maxIncomingMessageSize
        :returns:
            int
        :static:
        :description: QtWebSockets/QWebSocket-maxIncomingMessageSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.maxOutgoingFrameSize
        :returns:
            int
        :static:
        :description: QtWebSockets/QWebSocket-maxOutgoingFrameSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.open
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebSockets/QWebSocket-open-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.open
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
        :description: QtWebSockets/QWebSocket-open-f-1.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.open
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocketHandshakeOptions`
        :description: QtWebSockets/QWebSocket-open-f-2.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.open
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocketHandshakeOptions`
        :description: QtWebSockets/QWebSocket-open-f-3.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.origin
        :returns:
            str
        :description: QtWebSockets/QWebSocket-origin-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.outgoingFrameSize
        :returns:
            int
        :description: QtWebSockets/QWebSocket-outgoingFrameSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.pauseMode
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.PauseMode`
        :description: QtWebSockets/QWebSocket-pauseMode-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.peerAddress
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtWebSockets/QWebSocket-peerAddress-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.peerName
        :returns:
            str
        :description: QtWebSockets/QWebSocket-peerName-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.peerPort
        :returns:
            int
        :description: QtWebSockets/QWebSocket-peerPort-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.ping
        :args:
            payload: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
        :description: QtWebSockets/QWebSocket-ping-f-1.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.proxy
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtWebSockets/QWebSocket-proxy-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.readBufferSize
        :returns:
            int
        :description: QtWebSockets/QWebSocket-readBufferSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.request
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
        :description: QtWebSockets/QWebSocket-request-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.requestUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebSockets/QWebSocket-requestUrl-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.resourceName
        :returns:
            str
        :description: QtWebSockets/QWebSocket-resourceName-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.resume
        :description: QtWebSockets/QWebSocket-resume-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.sendBinaryMessage
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            int
        :description: QtWebSockets/QWebSocket-sendBinaryMessage-f-1.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.sendTextMessage
        :args:
            Optional[str]
        :returns:
            int
        :description: QtWebSockets/QWebSocket-sendTextMessage-f-1.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.setMaskGenerator
        :args:
            :sip:ref:`~PyQt6.QtWebSockets.QMaskGenerator`
        :description: QtWebSockets/QWebSocket-setMaskGenerator-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.setMaxAllowedIncomingFrameSize
        :args:
            int
        :description: QtWebSockets/QWebSocket-setMaxAllowedIncomingFrameSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.setMaxAllowedIncomingMessageSize
        :args:
            int
        :description: QtWebSockets/QWebSocket-setMaxAllowedIncomingMessageSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.setOutgoingFrameSize
        :args:
            int
        :description: QtWebSockets/QWebSocket-setOutgoingFrameSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.setPauseMode
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.PauseMode`
        :description: QtWebSockets/QWebSocket-setPauseMode-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.setProxy
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtWebSockets/QWebSocket-setProxy-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.setReadBufferSize
        :args:
            int
        :description: QtWebSockets/QWebSocket-setReadBufferSize-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.setSslConfiguration
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtWebSockets/QWebSocket-setSslConfiguration-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.sslConfiguration
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtWebSockets/QWebSocket-sslConfiguration-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.state
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState`
        :description: QtWebSockets/QWebSocket-state-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.subprotocol
        :returns:
            str
        :description: QtWebSockets/QWebSocket-subprotocol-f.rst

    .. sip:method:: PyQt6.QtWebSockets.QWebSocket.version
        :returns:
            :sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.Version`
        :description: QtWebSockets/QWebSocket-version-f.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.aboutToClose
        :description: QtWebSockets/QWebSocket-aboutToClose-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.alertReceived
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertLevel`
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertType`
            Optional[str]
        :description: QtWebSockets/QWebSocket-alertReceived-s-1.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.alertSent
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertLevel`
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertType`
            Optional[str]
        :description: QtWebSockets/QWebSocket-alertSent-s-1.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.authenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAuthenticator`
        :description: QtWebSockets/QWebSocket-authenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.binaryFrameReceived
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            bool
        :description: QtWebSockets/QWebSocket-binaryFrameReceived-s-1.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.binaryMessageReceived
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtWebSockets/QWebSocket-binaryMessageReceived-s-1.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.bytesWritten
        :args:
            int
        :description: QtWebSockets/QWebSocket-bytesWritten-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.connected
        :description: QtWebSockets/QWebSocket-connected-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.disconnected
        :description: QtWebSockets/QWebSocket-disconnected-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.error
        :description: QtWebSockets/QWebSocket-error-f-1.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.error
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtWebSockets/QWebSocket-error-f.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtWebSockets/QWebSocket-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.handshakeInterruptedOnError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslError`
        :description: QtWebSockets/QWebSocket-handshakeInterruptedOnError-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.peerVerifyError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslError`
        :description: QtWebSockets/QWebSocket-peerVerifyError-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.pong
        :args:
            int
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtWebSockets/QWebSocket-pong-s-1.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.preSharedKeyAuthenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator`
        :description: QtWebSockets/QWebSocket-preSharedKeyAuthenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.proxyAuthenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
            :sip:ref:`~PyQt6.QtNetwork.QAuthenticator`
        :description: QtWebSockets/QWebSocket-proxyAuthenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.readChannelFinished
        :description: QtWebSockets/QWebSocket-readChannelFinished-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.sslErrors
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslError`]
        :description: QtWebSockets/QWebSocket-sslErrors-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.stateChanged
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState`
        :description: QtWebSockets/QWebSocket-stateChanged-s.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.textFrameReceived
        :args:
            Optional[str]
            bool
        :description: QtWebSockets/QWebSocket-textFrameReceived-s-1.rst

    .. sip:signal:: PyQt6.QtWebSockets.QWebSocket.textMessageReceived
        :args:
            Optional[str]
        :description: QtWebSockets/QWebSocket-textMessageReceived-s-1.rst
