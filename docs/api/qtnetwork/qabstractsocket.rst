:orphan:

.. sip:class:: PyQt6.QtNetwork.QAbstractSocket
    :inherits: :sip:ref:`~PyQt6.QtCore.QIODevice`
    :description: QtNetwork/QAbstractSocket-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QAbstractSocket.BindFlag
        :description: QtNetwork/QAbstractSocket-BindFlag-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.BindFlag.DefaultForPlatform
            :description: QtNetwork/QAbstractSocket-BindFlag-DefaultForPlatform-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.BindFlag.DontShareAddress
            :description: QtNetwork/QAbstractSocket-BindFlag-DontShareAddress-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.BindFlag.ReuseAddressHint
            :description: QtNetwork/QAbstractSocket-BindFlag-ReuseAddressHint-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.BindFlag.ShareAddress
            :description: QtNetwork/QAbstractSocket-BindFlag-ShareAddress-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol
        :description: QtNetwork/QAbstractSocket-NetworkLayerProtocol-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol
            :description: QtNetwork/QAbstractSocket-NetworkLayerProtocol-AnyIPProtocol-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.IPv4Protocol
            :description: QtNetwork/QAbstractSocket-NetworkLayerProtocol-IPv4Protocol-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.IPv6Protocol
            :description: QtNetwork/QAbstractSocket-NetworkLayerProtocol-IPv6Protocol-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.UnknownNetworkLayerProtocol
            :description: QtNetwork/QAbstractSocket-NetworkLayerProtocol-UnknownNetworkLayerProtocol-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QAbstractSocket.PauseMode
        :description: QtNetwork/QAbstractSocket-PauseMode-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.PauseMode.PauseNever
            :description: QtNetwork/QAbstractSocket-PauseMode-PauseNever-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.PauseMode.PauseOnSslErrors
            :description: QtNetwork/QAbstractSocket-PauseMode-PauseOnSslErrors-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QAbstractSocket.SocketError
        :description: QtNetwork/QAbstractSocket-SocketError-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.AddressInUseError
            :description: QtNetwork/QAbstractSocket-SocketError-AddressInUseError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.ConnectionRefusedError
            :description: QtNetwork/QAbstractSocket-SocketError-ConnectionRefusedError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.DatagramTooLargeError
            :description: QtNetwork/QAbstractSocket-SocketError-DatagramTooLargeError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.HostNotFoundError
            :description: QtNetwork/QAbstractSocket-SocketError-HostNotFoundError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.NetworkError
            :description: QtNetwork/QAbstractSocket-SocketError-NetworkError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.OperationError
            :description: QtNetwork/QAbstractSocket-SocketError-OperationError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.ProxyAuthenticationRequiredError
            :description: QtNetwork/QAbstractSocket-SocketError-ProxyAuthenticationRequiredError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.ProxyConnectionClosedError
            :description: QtNetwork/QAbstractSocket-SocketError-ProxyConnectionClosedError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.ProxyConnectionRefusedError
            :description: QtNetwork/QAbstractSocket-SocketError-ProxyConnectionRefusedError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.ProxyConnectionTimeoutError
            :description: QtNetwork/QAbstractSocket-SocketError-ProxyConnectionTimeoutError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.ProxyNotFoundError
            :description: QtNetwork/QAbstractSocket-SocketError-ProxyNotFoundError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.ProxyProtocolError
            :description: QtNetwork/QAbstractSocket-SocketError-ProxyProtocolError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.RemoteHostClosedError
            :description: QtNetwork/QAbstractSocket-SocketError-RemoteHostClosedError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.SocketAccessError
            :description: QtNetwork/QAbstractSocket-SocketError-SocketAccessError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.SocketAddressNotAvailableError
            :description: QtNetwork/QAbstractSocket-SocketError-SocketAddressNotAvailableError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.SocketResourceError
            :description: QtNetwork/QAbstractSocket-SocketError-SocketResourceError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.SocketTimeoutError
            :description: QtNetwork/QAbstractSocket-SocketError-SocketTimeoutError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.SslHandshakeFailedError
            :description: QtNetwork/QAbstractSocket-SocketError-SslHandshakeFailedError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.SslInternalError
            :description: QtNetwork/QAbstractSocket-SocketError-SslInternalError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.SslInvalidUserDataError
            :description: QtNetwork/QAbstractSocket-SocketError-SslInvalidUserDataError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.TemporaryError
            :description: QtNetwork/QAbstractSocket-SocketError-TemporaryError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.UnfinishedSocketOperationError
            :description: QtNetwork/QAbstractSocket-SocketError-UnfinishedSocketOperationError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.UnknownSocketError
            :description: QtNetwork/QAbstractSocket-SocketError-UnknownSocketError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketError.UnsupportedSocketOperationError
            :description: QtNetwork/QAbstractSocket-SocketError-UnsupportedSocketOperationError-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QAbstractSocket.SocketOption
        :description: QtNetwork/QAbstractSocket-SocketOption-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketOption.KeepAliveOption
            :description: QtNetwork/QAbstractSocket-SocketOption-KeepAliveOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketOption.LowDelayOption
            :description: QtNetwork/QAbstractSocket-SocketOption-LowDelayOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketOption.MulticastLoopbackOption
            :description: QtNetwork/QAbstractSocket-SocketOption-MulticastLoopbackOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketOption.MulticastTtlOption
            :description: QtNetwork/QAbstractSocket-SocketOption-MulticastTtlOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketOption.PathMtuSocketOption
            :description: QtNetwork/QAbstractSocket-SocketOption-PathMtuSocketOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketOption.ReceiveBufferSizeSocketOption
            :description: QtNetwork/QAbstractSocket-SocketOption-ReceiveBufferSizeSocketOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketOption.SendBufferSizeSocketOption
            :description: QtNetwork/QAbstractSocket-SocketOption-SendBufferSizeSocketOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketOption.TypeOfServiceOption
            :description: QtNetwork/QAbstractSocket-SocketOption-TypeOfServiceOption-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QAbstractSocket.SocketState
        :description: QtNetwork/QAbstractSocket-SocketState-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketState.BoundState
            :description: QtNetwork/QAbstractSocket-SocketState-BoundState-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketState.ClosingState
            :description: QtNetwork/QAbstractSocket-SocketState-ClosingState-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState
            :description: QtNetwork/QAbstractSocket-SocketState-ConnectedState-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectingState
            :description: QtNetwork/QAbstractSocket-SocketState-ConnectingState-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketState.HostLookupState
            :description: QtNetwork/QAbstractSocket-SocketState-HostLookupState-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketState.ListeningState
            :description: QtNetwork/QAbstractSocket-SocketState-ListeningState-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketState.UnconnectedState
            :description: QtNetwork/QAbstractSocket-SocketState-UnconnectedState-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QAbstractSocket.SocketType
        :description: QtNetwork/QAbstractSocket-SocketType-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketType.SctpSocket
            :description: QtNetwork/QAbstractSocket-SocketType-SctpSocket-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketType.TcpSocket
            :description: QtNetwork/QAbstractSocket-SocketType-TcpSocket-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketType.UdpSocket
            :description: QtNetwork/QAbstractSocket-SocketType-UdpSocket-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QAbstractSocket.SocketType.UnknownSocketType
            :description: QtNetwork/QAbstractSocket-SocketType-UnknownSocketType-v.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketType`
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtNetwork/QAbstractSocket-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.abort
        :description: QtNetwork/QAbstractSocket-abort-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.bind
        :args:
            port: int = 0
            mode: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.BindFlag` = :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.BindFlag.DefaultForPlatform`
        :returns:
            bool
        :description: QtNetwork/QAbstractSocket-bind-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.bind
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
            port: int = 0
            mode: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.BindFlag` = :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.BindFlag.DefaultForPlatform`
        :returns:
            bool
        :description: QtNetwork/QAbstractSocket-bind-f-3.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.bytesAvailable
        :returns:
            int
        :description: QtNetwork/QAbstractSocket-bytesAvailable-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.bytesToWrite
        :returns:
            int
        :description: QtNetwork/QAbstractSocket-bytesToWrite-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.close
        :description: QtNetwork/QAbstractSocket-close-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.connectToHost
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
            int
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
        :description: QtNetwork/QAbstractSocket-connectToHost-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.connectToHost
        :args:
            str
            int
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
            protocol: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol` = :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol`
        :description: QtNetwork/QAbstractSocket-connectToHost-f-3.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.disconnectFromHost
        :description: QtNetwork/QAbstractSocket-disconnectFromHost-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.error
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtNetwork/QAbstractSocket-error-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.flush
        :returns:
            bool
        :description: QtNetwork/QAbstractSocket-flush-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.isSequential
        :returns:
            bool
        :description: QtNetwork/QAbstractSocket-isSequential-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.isValid
        :returns:
            bool
        :description: QtNetwork/QAbstractSocket-isValid-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.localAddress
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtNetwork/QAbstractSocket-localAddress-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.localPort
        :returns:
            int
        :description: QtNetwork/QAbstractSocket-localPort-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.pauseMode
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.PauseMode`
        :description: QtNetwork/QAbstractSocket-pauseMode-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.peerAddress
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtNetwork/QAbstractSocket-peerAddress-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.peerName
        :returns:
            str
        :description: QtNetwork/QAbstractSocket-peerName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.peerPort
        :returns:
            int
        :description: QtNetwork/QAbstractSocket-peerPort-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.protocolTag
        :returns:
            str
        :description: QtNetwork/QAbstractSocket-protocolTag-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.proxy
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtNetwork/QAbstractSocket-proxy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.readBufferSize
        :returns:
            int
        :description: QtNetwork/QAbstractSocket-readBufferSize-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.readData
        :args:
            int
        :returns:
            bytes
        :description: QtNetwork/QAbstractSocket-readData-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.readLineData
        :args:
            int
        :returns:
            bytes
        :description: QtNetwork/QAbstractSocket-readLineData-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.resume
        :description: QtNetwork/QAbstractSocket-resume-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setLocalAddress
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :description: QtNetwork/QAbstractSocket-setLocalAddress-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setLocalPort
        :args:
            int
        :description: QtNetwork/QAbstractSocket-setLocalPort-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setPauseMode
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.PauseMode`
        :description: QtNetwork/QAbstractSocket-setPauseMode-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setPeerAddress
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :description: QtNetwork/QAbstractSocket-setPeerAddress-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setPeerName
        :args:
            str
        :description: QtNetwork/QAbstractSocket-setPeerName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setPeerPort
        :args:
            int
        :description: QtNetwork/QAbstractSocket-setPeerPort-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setProtocolTag
        :args:
            str
        :description: QtNetwork/QAbstractSocket-setProtocolTag-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setProxy
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtNetwork/QAbstractSocket-setProxy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setReadBufferSize
        :args:
            int
        :description: QtNetwork/QAbstractSocket-setReadBufferSize-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setSocketDescriptor
        :args:
            :py:class:`~PyQt6.sip.voidptr`
            state: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState` = :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState`
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
        :returns:
            bool
        :description: QtNetwork/QAbstractSocket-setSocketDescriptor-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setSocketError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtNetwork/QAbstractSocket-setSocketError-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setSocketOption
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketOption`
            Any
        :description: QtNetwork/QAbstractSocket-setSocketOption-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.setSocketState
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState`
        :description: QtNetwork/QAbstractSocket-setSocketState-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.skipData
        :args:
            int
        :returns:
            int
        :description: QtNetwork/QAbstractSocket-skipData-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.socketDescriptor
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtNetwork/QAbstractSocket-socketDescriptor-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.socketOption
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketOption`
        :returns:
            Any
        :description: QtNetwork/QAbstractSocket-socketOption-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.socketType
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketType`
        :description: QtNetwork/QAbstractSocket-socketType-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.state
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState`
        :description: QtNetwork/QAbstractSocket-state-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.waitForBytesWritten
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtNetwork/QAbstractSocket-waitForBytesWritten-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.waitForConnected
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtNetwork/QAbstractSocket-waitForConnected-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.waitForDisconnected
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtNetwork/QAbstractSocket-waitForDisconnected-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.waitForReadyRead
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtNetwork/QAbstractSocket-waitForReadyRead-f.rst

    .. sip:method:: PyQt6.QtNetwork.QAbstractSocket.writeData
        :args:
            Union[bytes, bytearray, memoryview, PyQt6.sip.array, PyQt6.sip.voidptr]
        :returns:
            int
        :description: QtNetwork/QAbstractSocket-writeData-f-1.rst

    .. sip:signal:: PyQt6.QtNetwork.QAbstractSocket.connected
        :description: QtNetwork/QAbstractSocket-connected-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QAbstractSocket.disconnected
        :description: QtNetwork/QAbstractSocket-disconnected-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QAbstractSocket.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtNetwork/QAbstractSocket-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QAbstractSocket.hostFound
        :description: QtNetwork/QAbstractSocket-hostFound-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QAbstractSocket.proxyAuthenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
            :sip:ref:`~PyQt6.QtNetwork.QAuthenticator`
        :description: QtNetwork/QAbstractSocket-proxyAuthenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QAbstractSocket.stateChanged
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState`
        :description: QtNetwork/QAbstractSocket-stateChanged-s.rst
