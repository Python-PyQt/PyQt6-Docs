:orphan:

.. sip:class:: PyQt6.QtNetworkAuth.QOAuth1
    :inherits: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth`
    :description: QtNetworkAuth/QOAuth1-c.rst

    .. sip:enum:: PyQt6.QtNetworkAuth.QOAuth1.SignatureMethod
        :description: QtNetworkAuth/QOAuth1-SignatureMethod-e.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth1.SignatureMethod.Hmac_Sha1
            :description: QtNetworkAuth/QOAuth1-SignatureMethod-Hmac_Sha1-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth1.SignatureMethod.PlainText
            :description: QtNetworkAuth/QOAuth1-SignatureMethod-PlainText-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth1.SignatureMethod.Rsa_Sha1
            :description: QtNetworkAuth/QOAuth1-SignatureMethod-Rsa_Sha1-v.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QOAuth1-__init__-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QOAuth1-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.__init__
        :args:
            Optional[str]
            Optional[str]
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QOAuth1-__init__-f-3.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.clientCredentials
        :returns:
            Tuple[str, str]
        :description: QtNetworkAuth/QOAuth1-clientCredentials-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.clientSharedSecret
        :returns:
            str
        :description: QtNetworkAuth/QOAuth1-clientSharedSecret-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.continueGrantWithVerifier
        :args:
            Optional[str]
        :description: QtNetworkAuth/QOAuth1-continueGrantWithVerifier-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.deleteResource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QOAuth1-deleteResource-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.generateAuthorizationHeader
        :args:
            Dict[Optional[str], Any]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtNetworkAuth/QOAuth1-generateAuthorizationHeader-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.get
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QOAuth1-get-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.grant
        :description: QtNetworkAuth/QOAuth1-grant-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.head
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QOAuth1-head-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.nonce
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtNetworkAuth/QOAuth1-nonce-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.post
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QOAuth1-post-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.prepareRequest
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            body: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
        :description: QtNetworkAuth/QOAuth1-prepareRequest-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.put
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QOAuth1-put-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.requestTemporaryCredentials
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.Operation`
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parameters: Dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QOAuth1-requestTemporaryCredentials-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.requestTokenCredentials
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.Operation`
            :sip:ref:`~PyQt6.QtCore.QUrl`
            Tuple[Optional[str], Optional[str]]
            parameters: Dict[Optional[str], Any] = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QOAuth1-requestTokenCredentials-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setClientCredentials
        :args:
            Tuple[Optional[str], Optional[str]]
        :description: QtNetworkAuth/QOAuth1-setClientCredentials-f-2.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setClientCredentials
        :args:
            Optional[str]
            Optional[str]
        :description: QtNetworkAuth/QOAuth1-setClientCredentials-f-3.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setClientSharedSecret
        :args:
            Optional[str]
        :description: QtNetworkAuth/QOAuth1-setClientSharedSecret-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setSignatureMethod
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1.SignatureMethod`
        :description: QtNetworkAuth/QOAuth1-setSignatureMethod-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setTemporaryCredentialsUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth1-setTemporaryCredentialsUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setTokenCredentials
        :args:
            Tuple[Optional[str], Optional[str]]
        :description: QtNetworkAuth/QOAuth1-setTokenCredentials-f-2.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setTokenCredentials
        :args:
            Optional[str]
            Optional[str]
        :description: QtNetworkAuth/QOAuth1-setTokenCredentials-f-3.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setTokenCredentialsUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth1-setTokenCredentialsUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setTokenSecret
        :args:
            Optional[str]
        :description: QtNetworkAuth/QOAuth1-setTokenSecret-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setup
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            Dict[Optional[str], Any]
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.Operation`
        :description: QtNetworkAuth/QOAuth1-setup-f-2.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.setup
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            Dict[Optional[str], Any]
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtNetworkAuth/QOAuth1-setup-f-3.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.signatureMethod
        :returns:
            :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1.SignatureMethod`
        :description: QtNetworkAuth/QOAuth1-signatureMethod-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.temporaryCredentialsUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth1-temporaryCredentialsUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.tokenCredentials
        :returns:
            Tuple[str, str]
        :description: QtNetworkAuth/QOAuth1-tokenCredentials-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.tokenCredentialsUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth1-tokenCredentialsUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1.tokenSecret
        :returns:
            str
        :description: QtNetworkAuth/QOAuth1-tokenSecret-f.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth1.clientSharedSecretChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QOAuth1-clientSharedSecretChanged-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth1.signatureMethodChanged
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1.SignatureMethod`
        :description: QtNetworkAuth/QOAuth1-signatureMethodChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth1.temporaryCredentialsUrlChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth1-temporaryCredentialsUrlChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth1.tokenCredentialsUrlChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth1-tokenCredentialsUrlChanged-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QOAuth1.tokenSecretChanged
        :args:
            Optional[str]
        :description: QtNetworkAuth/QOAuth1-tokenSecretChanged-s-1.rst
