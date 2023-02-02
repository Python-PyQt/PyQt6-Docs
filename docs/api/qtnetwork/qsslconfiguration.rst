:orphan:

.. sip:class:: PyQt6.QtNetwork.QSslConfiguration
    :description: QtNetwork/QSslConfiguration-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus
        :description: QtNetwork/QSslConfiguration-NextProtocolNegotiationStatus-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus.NextProtocolNegotiationNegotiated
            :description: QtNetwork/QSslConfiguration-NextProtocolNegotiationStatus-NextProtocolNegotiationNegotiated-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus.NextProtocolNegotiationNone
            :description: QtNetwork/QSslConfiguration-NextProtocolNegotiationStatus-NextProtocolNegotiationNone-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus.NextProtocolNegotiationUnsupported
            :description: QtNetwork/QSslConfiguration-NextProtocolNegotiationStatus-NextProtocolNegotiationUnsupported-v.rst

    .. sip:attribute:: PyQt6.QtNetwork.QSslConfiguration.NextProtocolHttp1_1
        :type: bytes
        :const:
        :static:
        :description: QtNetwork/QSslConfiguration-NextProtocolHttp1_1-a.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.__init__
        :description: QtNetwork/QSslConfiguration-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtNetwork/QSslConfiguration-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.addCaCertificate
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :description: QtNetwork/QSslConfiguration-addCaCertificate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.addCaCertificates
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtNetwork/QSslConfiguration-addCaCertificates-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.addCaCertificates
        :args:
            str
            format: :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat` = :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat.Pem`
            syntax: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.PatternSyntax` = :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.PatternSyntax.FixedString`
        :returns:
            bool
        :description: QtNetwork/QSslConfiguration-addCaCertificates-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.allowedNextProtocols
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtNetwork/QSslConfiguration-allowedNextProtocols-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.backendConfiguration
        :returns:
            Dict[:sip:ref:`~PyQt6.QtCore.QByteArray`, Any]
        :description: QtNetwork/QSslConfiguration-backendConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.caCertificates
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtNetwork/QSslConfiguration-caCertificates-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.ciphers
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCipher`]
        :description: QtNetwork/QSslConfiguration-ciphers-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.defaultConfiguration
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :static:
        :description: QtNetwork/QSslConfiguration-defaultConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.defaultDtlsConfiguration
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :static:
        :description: QtNetwork/QSslConfiguration-defaultDtlsConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.diffieHellmanParameters
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters`
        :description: QtNetwork/QSslConfiguration-diffieHellmanParameters-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.dtlsCookieVerificationEnabled
        :returns:
            bool
        :description: QtNetwork/QSslConfiguration-dtlsCookieVerificationEnabled-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.ellipticCurves
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve`]
        :description: QtNetwork/QSslConfiguration-ellipticCurves-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.ephemeralServerKey
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslKey`
        :description: QtNetwork/QSslConfiguration-ephemeralServerKey-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.__eq__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :returns:
            bool
        :description: QtNetwork/QSslConfiguration-__eq__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.handshakeMustInterruptOnError
        :returns:
            bool
        :description: QtNetwork/QSslConfiguration-handshakeMustInterruptOnError-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.isNull
        :returns:
            bool
        :description: QtNetwork/QSslConfiguration-isNull-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.localCertificate
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :description: QtNetwork/QSslConfiguration-localCertificate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.localCertificateChain
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtNetwork/QSslConfiguration-localCertificateChain-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.missingCertificateIsFatal
        :returns:
            bool
        :description: QtNetwork/QSslConfiguration-missingCertificateIsFatal-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.__ne__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :returns:
            bool
        :description: QtNetwork/QSslConfiguration-__ne__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.nextNegotiatedProtocol
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QSslConfiguration-nextNegotiatedProtocol-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.nextProtocolNegotiationStatus
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus`
        :description: QtNetwork/QSslConfiguration-nextProtocolNegotiationStatus-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.ocspStaplingEnabled
        :returns:
            bool
        :description: QtNetwork/QSslConfiguration-ocspStaplingEnabled-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.peerCertificate
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :description: QtNetwork/QSslConfiguration-peerCertificate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.peerCertificateChain
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtNetwork/QSslConfiguration-peerCertificateChain-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.peerVerifyDepth
        :returns:
            int
        :description: QtNetwork/QSslConfiguration-peerVerifyDepth-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.peerVerifyMode
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket.PeerVerifyMode`
        :description: QtNetwork/QSslConfiguration-peerVerifyMode-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.preSharedKeyIdentityHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QSslConfiguration-preSharedKeyIdentityHint-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.privateKey
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslKey`
        :description: QtNetwork/QSslConfiguration-privateKey-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.protocol
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol`
        :description: QtNetwork/QSslConfiguration-protocol-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.sessionCipher
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslCipher`
        :description: QtNetwork/QSslConfiguration-sessionCipher-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.sessionProtocol
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol`
        :description: QtNetwork/QSslConfiguration-sessionProtocol-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.sessionTicket
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QSslConfiguration-sessionTicket-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.sessionTicketLifeTimeHint
        :returns:
            int
        :description: QtNetwork/QSslConfiguration-sessionTicketLifeTimeHint-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setAllowedNextProtocols
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtNetwork/QSslConfiguration-setAllowedNextProtocols-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setBackendConfiguration
        :args:
            backendConfiguration: Dict[:sip:ref:`~PyQt6.QtCore.QByteArray`, Any] = {}
        :description: QtNetwork/QSslConfiguration-setBackendConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setBackendConfigurationOption
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            Any
        :description: QtNetwork/QSslConfiguration-setBackendConfigurationOption-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setCaCertificates
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtNetwork/QSslConfiguration-setCaCertificates-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setCiphers
        :args:
            str
        :description: QtNetwork/QSslConfiguration-setCiphers-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setCiphers
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslCipher`]
        :description: QtNetwork/QSslConfiguration-setCiphers-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setDefaultConfiguration
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :static:
        :description: QtNetwork/QSslConfiguration-setDefaultConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setDefaultDtlsConfiguration
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :static:
        :description: QtNetwork/QSslConfiguration-setDefaultDtlsConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setDiffieHellmanParameters
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslDiffieHellmanParameters`
        :description: QtNetwork/QSslConfiguration-setDiffieHellmanParameters-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setDtlsCookieVerificationEnabled
        :args:
            bool
        :description: QtNetwork/QSslConfiguration-setDtlsCookieVerificationEnabled-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setEllipticCurves
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve`]
        :description: QtNetwork/QSslConfiguration-setEllipticCurves-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setHandshakeMustInterruptOnError
        :args:
            bool
        :description: QtNetwork/QSslConfiguration-setHandshakeMustInterruptOnError-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setLocalCertificate
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :description: QtNetwork/QSslConfiguration-setLocalCertificate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setLocalCertificateChain
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtNetwork/QSslConfiguration-setLocalCertificateChain-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setMissingCertificateIsFatal
        :args:
            bool
        :description: QtNetwork/QSslConfiguration-setMissingCertificateIsFatal-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setOcspStaplingEnabled
        :args:
            bool
        :description: QtNetwork/QSslConfiguration-setOcspStaplingEnabled-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setPeerVerifyDepth
        :args:
            int
        :description: QtNetwork/QSslConfiguration-setPeerVerifyDepth-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setPeerVerifyMode
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket.PeerVerifyMode`
        :description: QtNetwork/QSslConfiguration-setPeerVerifyMode-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setPreSharedKeyIdentityHint
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QSslConfiguration-setPreSharedKeyIdentityHint-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setPrivateKey
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslKey`
        :description: QtNetwork/QSslConfiguration-setPrivateKey-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setProtocol
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol`
        :description: QtNetwork/QSslConfiguration-setProtocol-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setSessionTicket
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QSslConfiguration-setSessionTicket-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.setSslOption
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.SslOption`
            bool
        :description: QtNetwork/QSslConfiguration-setSslOption-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.supportedCiphers
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCipher`]
        :static:
        :description: QtNetwork/QSslConfiguration-supportedCiphers-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.supportedEllipticCurves
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslEllipticCurve`]
        :static:
        :description: QtNetwork/QSslConfiguration-supportedEllipticCurves-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.swap
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtNetwork/QSslConfiguration-swap-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.systemCaCertificates
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :static:
        :description: QtNetwork/QSslConfiguration-systemCaCertificates-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslConfiguration.testSslOption
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSsl.SslOption`
        :returns:
            bool
        :description: QtNetwork/QSslConfiguration-testSslOption-f-1.rst
