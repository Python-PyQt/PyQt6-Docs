:orphan:

.. sip:class:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow
    :inherits: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth2`
    :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-c.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.__init__
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-__init__-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-__init__-f-2.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.completeVerificationUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-completeVerificationUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-event-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.grant
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-grant-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.isPolling
        :returns:
            bool
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-isPolling-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.refreshTokensImplementation
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-refreshTokensImplementation-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.startTokenPolling
        :returns:
            bool
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-startTokenPolling-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.stopTokenPolling
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-stopTokenPolling-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.userCode
        :returns:
            str
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-userCode-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.userCodeExpirationAt
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-userCodeExpirationAt-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.verificationUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-verificationUrl-f.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.authorizeWithUserCode
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-authorizeWithUserCode-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.completeVerificationUrlChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-completeVerificationUrlChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.pollingChanged
        :args:
            bool
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-pollingChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.userCodeChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-userCodeChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.userCodeExpirationAtChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-userCodeExpirationAtChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth2DeviceAuthorizationFlow.verificationUrlChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth2DeviceAuthorizationFlow-verificationUrlChanged-s.rst
