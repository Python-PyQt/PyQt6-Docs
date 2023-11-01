:orphan:

.. sip:class:: PyQt6.QtNetwork.QSslSocket
    :inherits: :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`
    :description: QtNetwork/QSslSocket-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QSslSocket.PeerVerifyMode
        :description: QtNetwork/QSslSocket-PeerVerifyMode-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslSocket.PeerVerifyMode.AutoVerifyPeer
            :description: QtNetwork/QSslSocket-PeerVerifyMode-AutoVerifyPeer-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslSocket.PeerVerifyMode.QueryPeer
            :description: QtNetwork/QSslSocket-PeerVerifyMode-QueryPeer-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslSocket.PeerVerifyMode.VerifyNone
            :description: QtNetwork/QSslSocket-PeerVerifyMode-VerifyNone-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslSocket.PeerVerifyMode.VerifyPeer
            :description: QtNetwork/QSslSocket-PeerVerifyMode-VerifyPeer-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QSslSocket.SslMode
        :description: QtNetwork/QSslSocket-SslMode-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslSocket.SslMode.SslClientMode
            :description: QtNetwork/QSslSocket-SslMode-SslClientMode-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslSocket.SslMode.SslServerMode
            :description: QtNetwork/QSslSocket-SslMode-SslServerMode-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslSocket.SslMode.UnencryptedMode
            :description: QtNetwork/QSslSocket-SslMode-UnencryptedMode-v.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetwork/QSslSocket-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.activeBackend
        :returns:
            str
        :static:
        :description: QtNetwork/QSslSocket-activeBackend-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.atEnd
        :returns:
            bool
        :description: QtNetwork/QSslSocket-atEnd-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.availableBackends
        :returns:
            List[str]
        :static:
        :description: QtNetwork/QSslSocket-availableBackends-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.bytesAvailable
        :returns:
            int
        :description: QtNetwork/QSslSocket-bytesAvailable-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.bytesToWrite
        :returns:
            int
        :description: QtNetwork/QSslSocket-bytesToWrite-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.canReadLine
        :returns:
            bool
        :description: QtNetwork/QSslSocket-canReadLine-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.close
        :description: QtNetwork/QSslSocket-close-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.connectToHost
        :args:
            Optional[str]
            int
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
            protocol: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol` = :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol`
        :description: QtNetwork/QSslSocket-connectToHost-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted
        :args:
            Optional[str]
            int
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
            protocol: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol` = :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol`
        :description: QtNetwork/QSslSocket-connectToHostEncrypted-f-4.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted
        :args:
            Optional[str]
            int
            Optional[str]
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
            protocol: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol` = :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol`
        :description: QtNetwork/QSslSocket-connectToHostEncrypted-f-5.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.continueInterruptedHandshake
        :description: QtNetwork/QSslSocket-continueInterruptedHandshake-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.disconnectFromHost
        :description: QtNetwork/QSslSocket-disconnectFromHost-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.encryptedBytesAvailable
        :returns:
            int
        :description: QtNetwork/QSslSocket-encryptedBytesAvailable-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.encryptedBytesToWrite
        :returns:
            int
        :description: QtNetwork/QSslSocket-encryptedBytesToWrite-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.ignoreSslErrors
        :description: QtNetwork/QSslSocket-ignoreSslErrors-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.ignoreSslErrors
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslError`]
        :description: QtNetwork/QSslSocket-ignoreSslErrors-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.implementedClasses
        :args:
            backendName: Optional[str] = ''
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSsl.ImplementedClass`]
        :static:
        :description: QtNetwork/QSslSocket-implementedClasses-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.isClassImplemented
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.ImplementedClass`
            backendName: Optional[str] = ''
        :returns:
            bool
        :static:
        :description: QtNetwork/QSslSocket-isClassImplemented-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.isEncrypted
        :returns:
            bool
        :description: QtNetwork/QSslSocket-isEncrypted-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.isFeatureSupported
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.SupportedFeature`
            backendName: Optional[str] = ''
        :returns:
            bool
        :static:
        :description: QtNetwork/QSslSocket-isFeatureSupported-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.isProtocolSupported
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol`
            backendName: Optional[str] = ''
        :returns:
            bool
        :static:
        :description: QtNetwork/QSslSocket-isProtocolSupported-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.localCertificate
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :description: QtNetwork/QSslSocket-localCertificate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.localCertificateChain
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtNetwork/QSslSocket-localCertificateChain-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.mode
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket.SslMode`
        :description: QtNetwork/QSslSocket-mode-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.ocspResponses
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QOcspResponse`]
        :description: QtNetwork/QSslSocket-ocspResponses-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.peerCertificate
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :description: QtNetwork/QSslSocket-peerCertificate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.peerCertificateChain
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtNetwork/QSslSocket-peerCertificateChain-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.peerVerifyDepth
        :returns:
            int
        :description: QtNetwork/QSslSocket-peerVerifyDepth-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.peerVerifyMode
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket.PeerVerifyMode`
        :description: QtNetwork/QSslSocket-peerVerifyMode-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.peerVerifyName
        :returns:
            str
        :description: QtNetwork/QSslSocket-peerVerifyName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.privateKey
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslKey`
        :description: QtNetwork/QSslSocket-privateKey-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.protocol
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol`
        :description: QtNetwork/QSslSocket-protocol-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.readData
        :args:
            int
        :returns:
            bytes
        :description: QtNetwork/QSslSocket-readData-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.resume
        :description: QtNetwork/QSslSocket-resume-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.sessionCipher
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslCipher`
        :description: QtNetwork/QSslSocket-sessionCipher-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.sessionProtocol
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol`
        :description: QtNetwork/QSslSocket-sessionProtocol-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setActiveBackend
        :args:
            Optional[str]
        :returns:
            bool
        :static:
        :description: QtNetwork/QSslSocket-setActiveBackend-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setLocalCertificate
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :description: QtNetwork/QSslSocket-setLocalCertificate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setLocalCertificate
        :args:
            Optional[str]
            format: :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat` = :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat.Pem`
        :description: QtNetwork/QSslSocket-setLocalCertificate-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setLocalCertificateChain
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtNetwork/QSslSocket-setLocalCertificateChain-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setPeerVerifyDepth
        :args:
            int
        :description: QtNetwork/QSslSocket-setPeerVerifyDepth-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setPeerVerifyMode
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket.PeerVerifyMode`
        :description: QtNetwork/QSslSocket-setPeerVerifyMode-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setPeerVerifyName
        :args:
            Optional[str]
        :description: QtNetwork/QSslSocket-setPeerVerifyName-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setPrivateKey
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslKey`
        :description: QtNetwork/QSslSocket-setPrivateKey-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setPrivateKey
        :args:
            Optional[str]
            algorithm: :sip:ref:`~PyQt6.QtNetwork.QSsl.KeyAlgorithm` = :sip:ref:`~PyQt6.QtNetwork.QSsl.KeyAlgorithm.Rsa`
            format: :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat` = :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat.Pem`
            passPhrase: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
        :description: QtNetwork/QSslSocket-setPrivateKey-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setProtocol
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol`
        :description: QtNetwork/QSslSocket-setProtocol-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setReadBufferSize
        :args:
            int
        :description: QtNetwork/QSslSocket-setReadBufferSize-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setSocketDescriptor
        :args:
            :py:class:`~PyQt6.sip.voidptr`
            state: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState` = :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState`
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
        :returns:
            bool
        :description: QtNetwork/QSslSocket-setSocketDescriptor-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setSocketOption
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketOption`
            Any
        :description: QtNetwork/QSslSocket-setSocketOption-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.setSslConfiguration
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtNetwork/QSslSocket-setSslConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.skipData
        :args:
            int
        :returns:
            int
        :description: QtNetwork/QSslSocket-skipData-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.socketOption
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketOption`
        :returns:
            Any
        :description: QtNetwork/QSslSocket-socketOption-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.sslConfiguration
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtNetwork/QSslSocket-sslConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.sslHandshakeErrors
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslError`]
        :description: QtNetwork/QSslSocket-sslHandshakeErrors-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.sslLibraryBuildVersionNumber
        :returns:
            int
        :static:
        :description: QtNetwork/QSslSocket-sslLibraryBuildVersionNumber-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.sslLibraryBuildVersionString
        :returns:
            str
        :static:
        :description: QtNetwork/QSslSocket-sslLibraryBuildVersionString-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.sslLibraryVersionNumber
        :returns:
            int
        :static:
        :description: QtNetwork/QSslSocket-sslLibraryVersionNumber-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.sslLibraryVersionString
        :returns:
            str
        :static:
        :description: QtNetwork/QSslSocket-sslLibraryVersionString-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.startClientEncryption
        :description: QtNetwork/QSslSocket-startClientEncryption-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.startServerEncryption
        :description: QtNetwork/QSslSocket-startServerEncryption-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.supportedFeatures
        :args:
            backendName: Optional[str] = ''
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSsl.SupportedFeature`]
        :static:
        :description: QtNetwork/QSslSocket-supportedFeatures-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.supportedProtocols
        :args:
            backendName: Optional[str] = ''
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol`]
        :static:
        :description: QtNetwork/QSslSocket-supportedProtocols-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.supportsSsl
        :returns:
            bool
        :static:
        :description: QtNetwork/QSslSocket-supportsSsl-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.waitForBytesWritten
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtNetwork/QSslSocket-waitForBytesWritten-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.waitForConnected
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtNetwork/QSslSocket-waitForConnected-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.waitForDisconnected
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtNetwork/QSslSocket-waitForDisconnected-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.waitForEncrypted
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtNetwork/QSslSocket-waitForEncrypted-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.waitForReadyRead
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtNetwork/QSslSocket-waitForReadyRead-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslSocket.writeData
        :args:
            Union[bytes, bytearray, memoryview, PyQt6.sip.array, PyQt6.sip.voidptr]
        :returns:
            int
        :description: QtNetwork/QSslSocket-writeData-f-1.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslSocket.alertReceived
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertLevel`
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertType`
            Optional[str]
        :description: QtNetwork/QSslSocket-alertReceived-s-1.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslSocket.alertSent
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertLevel`
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertType`
            Optional[str]
        :description: QtNetwork/QSslSocket-alertSent-s-1.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslSocket.encrypted
        :description: QtNetwork/QSslSocket-encrypted-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslSocket.encryptedBytesWritten
        :args:
            int
        :description: QtNetwork/QSslSocket-encryptedBytesWritten-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslSocket.handshakeInterruptedOnError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslError`
        :description: QtNetwork/QSslSocket-handshakeInterruptedOnError-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslSocket.modeChanged
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket.SslMode`
        :description: QtNetwork/QSslSocket-modeChanged-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslSocket.newSessionTicketReceived
        :description: QtNetwork/QSslSocket-newSessionTicketReceived-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslSocket.peerVerifyError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslError`
        :description: QtNetwork/QSslSocket-peerVerifyError-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslSocket.preSharedKeyAuthenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator`
        :description: QtNetwork/QSslSocket-preSharedKeyAuthenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslSocket.sslErrors
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslError`]
        :description: QtNetwork/QSslSocket-sslErrors-s.rst
