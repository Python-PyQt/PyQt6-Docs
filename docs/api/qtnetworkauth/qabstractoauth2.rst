:orphan:

.. sip:class:: PyQt6.QtNetworkAuth.QAbstractOAuth2
    :inherits: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth`
    :description: QtNetworkAuth/QAbstractOAuth2-c.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QAbstractOAuth2-__init__-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QAbstractOAuth2-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.clientIdentifierSharedKey
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-clientIdentifierSharedKey-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.createAuthenticatedUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[str, Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth2-createAuthenticatedUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.deleteResource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[str, Any] = {}
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
            parameters: Dict[str, Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-get-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.head
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[str, Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-head-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.post
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[str, Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-post-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.post
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-post-f-1.rst

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
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            body: :sip:ref:`~PyQt6.QtCore.QByteArray` = QByteArray()
        :description: QtNetworkAuth/QAbstractOAuth2-prepareRequest-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.put
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[str, Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-put-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.put
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-put-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.put
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuth2-put-f-2.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshToken
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-refreshToken-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.responseType
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-responseType-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.scope
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-scope-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setClientIdentifierSharedKey
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-setClientIdentifierSharedKey-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setRefreshToken
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-setRefreshToken-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setResponseType
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-setResponseType-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setScope
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-setScope-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setState
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-setState-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.setUserAgent
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-setUserAgent-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.state
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-state-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuth2.userAgent
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-userAgent-f.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.authorizationCallbackReceived
        :args:
            Dict[str, Any]
        :description: QtNetworkAuth/QAbstractOAuth2-authorizationCallbackReceived-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.clientIdentifierSharedKeyChanged
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-clientIdentifierSharedKeyChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.error
        :args:
            str
            str
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QAbstractOAuth2-error-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.expirationAtChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :description: QtNetworkAuth/QAbstractOAuth2-expirationAtChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.refreshTokenChanged
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-refreshTokenChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.responseTypeChanged
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-responseTypeChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.scopeChanged
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-scopeChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.stateChanged
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-stateChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuth2.userAgentChanged
        :args:
            str
        :description: QtNetworkAuth/QAbstractOAuth2-userAgentChanged-s.rst
