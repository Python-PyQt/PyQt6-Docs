:orphan:

.. sip:class:: PyQt6.QtNetworkAuth.QAbstractOAuth
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtNetworkAuth/QAbstractOAuth-c.rst

    .. sip:enum:: PyQt6.QtNetworkAuth.QAbstractOAuth.ContentType
        :description: QtNetworkAuth/QAbstractOAuth-ContentType-e.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.ContentType.Json
            :description: QtNetworkAuth/QAbstractOAuth-ContentType-Json-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.ContentType.WwwFormUrlEncoded
            :description: QtNetworkAuth/QAbstractOAuth-ContentType-WwwFormUrlEncoded-v.rst

    .. sip:enum:: PyQt6.QtNetworkAuth.QAbstractOAuth.Error
        :description: QtNetworkAuth/QAbstractOAuth-Error-e.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Error.NetworkError
            :description: QtNetworkAuth/QAbstractOAuth-Error-NetworkError-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Error.NoError
            :description: QtNetworkAuth/QAbstractOAuth-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Error.OAuthCallbackNotVerified
            :description: QtNetworkAuth/QAbstractOAuth-Error-OAuthCallbackNotVerified-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Error.OAuthTokenNotFoundError
            :description: QtNetworkAuth/QAbstractOAuth-Error-OAuthTokenNotFoundError-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Error.OAuthTokenSecretNotFoundError
            :description: QtNetworkAuth/QAbstractOAuth-Error-OAuthTokenSecretNotFoundError-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Error.ServerError
            :description: QtNetworkAuth/QAbstractOAuth-Error-ServerError-v.rst

    .. sip:enum:: PyQt6.QtNetworkAuth.QAbstractOAuth.Stage
        :description: QtNetworkAuth/QAbstractOAuth-Stage-e.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Stage.RefreshingAccessToken
            :description: QtNetworkAuth/QAbstractOAuth-Stage-RefreshingAccessToken-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Stage.RequestingAccessToken
            :description: QtNetworkAuth/QAbstractOAuth-Stage-RequestingAccessToken-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Stage.RequestingAuthorization
            :description: QtNetworkAuth/QAbstractOAuth-Stage-RequestingAuthorization-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Stage.RequestingTemporaryCredentials
            :description: QtNetworkAuth/QAbstractOAuth-Stage-RequestingTemporaryCredentials-v.rst

    .. sip:enum:: PyQt6.QtNetworkAuth.QAbstractOAuth.Status
        :description: QtNetworkAuth/QAbstractOAuth-Status-e.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Status.Granted
            :description: QtNetworkAuth/QAbstractOAuth-Status-Granted-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Status.NotAuthenticated
            :description: QtNetworkAuth/QAbstractOAuth-Status-NotAuthenticated-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Status.RefreshingToken
            :description: QtNetworkAuth/QAbstractOAuth-Status-RefreshingToken-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QAbstractOAuth.Status.TemporaryCredentialsReceived
            :description: QtNetworkAuth/QAbstractOAuth-Status-TemporaryCredentialsReceived-v.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.authorizationUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth-authorizationUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.callback
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth-callback-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.clientIdentifier
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth-clientIdentifier-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.contentType
        :returns:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.ContentType`
        :description: QtNetworkAuth/QAbstractOAuth-contentType-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.deleteResource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[str, Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth-deleteResource-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.extraTokens
        :returns:
            Dict[str, Any]
        :description: QtNetworkAuth/QAbstractOAuth-extraTokens-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.generateRandomString
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtNetworkAuth/QAbstractOAuth-generateRandomString-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.get
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[str, Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth-get-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.grant
        :description: QtNetworkAuth/QAbstractOAuth-grant-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.head
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[str, Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth-head-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.modifyParametersFunction
        :returns:
            callable
        :description: QtNetworkAuth/QAbstractOAuth-modifyParametersFunction-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.networkAccessManager
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
        :description: QtNetworkAuth/QAbstractOAuth-networkAccessManager-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.post
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[str, Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth-post-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.prepareRequest
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            body: :sip:ref:`~PyQt6.QtCore.QByteArray` = QByteArray()
        :description: QtNetworkAuth/QAbstractOAuth-prepareRequest-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.put
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[str, Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth-put-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.replyHandler
        :returns:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler`
        :description: QtNetworkAuth/QAbstractOAuth-replyHandler-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.resourceOwnerAuthorization
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            unknown-type
        :description: QtNetworkAuth/QAbstractOAuth-resourceOwnerAuthorization-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.setAuthorizationUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth-setAuthorizationUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.setClientIdentifier
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth-setClientIdentifier-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.setContentType
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.ContentType`
        :description: QtNetworkAuth/QAbstractOAuth-setContentType-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.setModifyParametersFunction
        :args:
            callable
        :description: QtNetworkAuth/QAbstractOAuth-setModifyParametersFunction-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.setNetworkAccessManager
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
        :description: QtNetworkAuth/QAbstractOAuth-setNetworkAccessManager-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.setReplyHandler
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler`
        :description: QtNetworkAuth/QAbstractOAuth-setReplyHandler-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.setStatus
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status`
        :description: QtNetworkAuth/QAbstractOAuth-setStatus-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.setToken
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth-setToken-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.status
        :returns:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status`
        :description: QtNetworkAuth/QAbstractOAuth-status-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth.token
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth-token-f.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.authorizationUrlChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth-authorizationUrlChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.authorizeWithBrowser
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth-authorizeWithBrowser-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.clientIdentifierChanged
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth-clientIdentifierChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.contentTypeChanged
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.ContentType`
        :description: QtNetworkAuth/QAbstractOAuth-contentTypeChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.extraTokensChanged
        :args:
            Dict[str, Any]
        :description: QtNetworkAuth/QAbstractOAuth-extraTokensChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.finished
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth-finished-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.granted
        :description: QtNetworkAuth/QAbstractOAuth-granted-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.replyDataReceived
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetworkAuth/QAbstractOAuth-replyDataReceived-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.requestFailed
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Error`
        :description: QtNetworkAuth/QAbstractOAuth-requestFailed-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.statusChanged
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Status`
        :description: QtNetworkAuth/QAbstractOAuth-statusChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth.tokenChanged
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth-tokenChanged-s.rst
