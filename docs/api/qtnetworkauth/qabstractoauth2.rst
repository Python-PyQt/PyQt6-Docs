:orphan:

.. sip:class:: PyQt6.QtNetworkAuth.QAbstractOAuth2
    :inherits: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth`
    :description: QtNetworkAuth/QAbstractOAuth2-c.rst

    .. sip:enum:: PyQt6.QtNetworkAuth.QAbstractOAuth2.NonceMode
        :description: QtNetworkAuth/QAbstractOAuth2-NonceMode-e.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth2.NonceMode.Automatic
            :description: QtNetworkAuth/QAbstractOAuth2-NonceMode-Automatic-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth2.NonceMode.Disabled
            :description: QtNetworkAuth/QAbstractOAuth2-NonceMode-Disabled-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth2.NonceMode.Enabled
            :description: QtNetworkAuth/QAbstractOAuth2-NonceMode-Enabled-v.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QAbstractOAuth2-__init__-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QAbstractOAuth2-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.autoRefresh
        :returns:
            bool
        :description: QtNetworkAuth/QAbstractOAuth2-autoRefresh-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.clearNetworkRequestModifier
        :description: QtNetworkAuth/QAbstractOAuth2-clearNetworkRequestModifier-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.clientIdentifierSharedKey
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-clientIdentifierSharedKey-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.createAuthenticatedUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth2-createAuthenticatedUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.deleteResource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-deleteResource-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.expirationAt
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtNetworkAuth/QAbstractOAuth2-expirationAt-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.get
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-get-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.grantedScopeTokens
        :returns:
            set[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtNetworkAuth/QAbstractOAuth2-grantedScopeTokens-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.head
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-head-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.idToken
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-idToken-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.nonce
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-nonce-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.nonceMode
        :returns:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.NonceMode`
        :description: QtNetworkAuth/QAbstractOAuth2-nonceMode-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.post
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-post-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.post
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-post-f-4.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.post
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-post-f-2.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.prepareRequest
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            body: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
        :description: QtNetworkAuth/QAbstractOAuth2-prepareRequest-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.put
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-put-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.put
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-put-f-4.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.put
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-put-f-2.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshLeadTime
        :returns:
            int
        :description: QtNetworkAuth/QAbstractOAuth2-refreshLeadTime-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshToken
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-refreshToken-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshTokens
        :description: QtNetworkAuth/QAbstractOAuth2-refreshTokens-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshTokensImplementation
        :description: QtNetworkAuth/QAbstractOAuth2-refreshTokensImplementation-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.requestedScopeTokens
        :returns:
            set[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtNetworkAuth/QAbstractOAuth2-requestedScopeTokens-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.responseType
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-responseType-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.scope
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-scope-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setAutoRefresh
        :args:
            bool
        :description: QtNetworkAuth/QAbstractOAuth2-setAutoRefresh-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setClientIdentifierSharedKey
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-setClientIdentifierSharedKey-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setNonce
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-setNonce-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setNonceMode
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.NonceMode`
        :description: QtNetworkAuth/QAbstractOAuth2-setNonceMode-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setRefreshLeadTime
        :args:
            int
        :description: QtNetworkAuth/QAbstractOAuth2-setRefreshLeadTime-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setRefreshToken
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-setRefreshToken-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setRequestedScopeTokens
        :args:
            Iterable[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]]
        :description: QtNetworkAuth/QAbstractOAuth2-setRequestedScopeTokens-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setResponseType
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-setResponseType-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setScope
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-setScope-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setSslConfiguration
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtNetworkAuth/QAbstractOAuth2-setSslConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setState
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-setState-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setTokenUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth2-setTokenUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setUserAgent
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-setUserAgent-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.sslConfiguration
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtNetworkAuth/QAbstractOAuth2-sslConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.state
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-state-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.tokenUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth2-tokenUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.userAgent
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-userAgent-f.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.accessTokenAboutToExpire
        :description: QtNetworkAuth/QAbstractOAuth2-accessTokenAboutToExpire-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.authorizationCallbackReceived
        :args:
            dict[Optional[str], Any]
        :description: QtNetworkAuth/QAbstractOAuth2-authorizationCallbackReceived-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.autoRefreshChanged
        :args:
            bool
        :description: QtNetworkAuth/QAbstractOAuth2-autoRefreshChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.clientIdentifierSharedKeyChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-clientIdentifierSharedKeyChanged-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.error
        :args:
            Optional[str]
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth2-error-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.expirationAtChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :description: QtNetworkAuth/QAbstractOAuth2-expirationAtChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.grantedScopeTokensChanged
        :args:
            Iterable[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]]
        :description: QtNetworkAuth/QAbstractOAuth2-grantedScopeTokensChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.idTokenChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-idTokenChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.nonceChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-nonceChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.nonceModeChanged
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2.NonceMode`
        :description: QtNetworkAuth/QAbstractOAuth2-nonceModeChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshLeadTimeChanged
        :args:
            int
        :description: QtNetworkAuth/QAbstractOAuth2-refreshLeadTimeChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshTokenChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-refreshTokenChanged-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.requestedScopeTokensChanged
        :args:
            Iterable[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]]
        :description: QtNetworkAuth/QAbstractOAuth2-requestedScopeTokensChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.responseTypeChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-responseTypeChanged-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.scopeChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-scopeChanged-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.serverReportedErrorOccurred
        :args:
            Optional[str]
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth2-serverReportedErrorOccurred-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.sslConfigurationChanged
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtNetworkAuth/QAbstractOAuth2-sslConfigurationChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.stateChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-stateChanged-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.tokenUrlChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth2-tokenUrlChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.userAgentChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuth2-userAgentChanged-s-1.rst
