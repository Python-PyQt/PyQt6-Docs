:orphan:

.. sip:class:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow
    :inherits: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2`
    :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-c.rst

    .. sip:enum:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.PkceMethod
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-PkceMethod-e.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.PkceMethod.None_
            :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-PkceMethod-None_-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.PkceMethod.Plain
            :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-PkceMethod-Plain-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.PkceMethod.S256
            :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-PkceMethod-S256-v.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-__init__-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.__init__
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-__init__-f-5.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-__init__-f-3.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.__init__
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-__init__-f-6.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.accessTokenUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-accessTokenUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.buildAuthenticateUrl
        :args:
            parameters: dict[Optional[str], Sequence[Any]] = {}
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-buildAuthenticateUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.grant
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-grant-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.pkceMethod
        :returns:
            :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.PkceMethod`
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-pkceMethod-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.refreshAccessToken
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-refreshAccessToken-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.refreshTokensImplementation
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-refreshTokensImplementation-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.requestAccessToken
        :args:
            Optional[str]
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-requestAccessToken-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.resourceOwnerAuthorization
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: dict[Optional[str], Sequence[Any]] = {}
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-resourceOwnerAuthorization-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.setAccessTokenUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-setAccessTokenUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.setPkceMethod
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.PkceMethod`
            length: int = 43
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-setPkceMethod-f.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.accessTokenUrlChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth2AuthorizationCodeFlow-accessTokenUrlChanged-s.rst
