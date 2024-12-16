:orphan:

.. sip:class:: PyQt6.QtNetwork.QNetworkAccessManager
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtNetwork/QNetworkAccessManager-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkAccessManager.Operation
        :description: QtNetwork/QNetworkAccessManager-Operation-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkAccessManager.Operation.CustomOperation
            :description: QtNetwork/QNetworkAccessManager-Operation-CustomOperation-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkAccessManager.Operation.DeleteOperation
            :description: QtNetwork/QNetworkAccessManager-Operation-DeleteOperation-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkAccessManager.Operation.GetOperation
            :description: QtNetwork/QNetworkAccessManager-Operation-GetOperation-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkAccessManager.Operation.HeadOperation
            :description: QtNetwork/QNetworkAccessManager-Operation-HeadOperation-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkAccessManager.Operation.PostOperation
            :description: QtNetwork/QNetworkAccessManager-Operation-PostOperation-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkAccessManager.Operation.PutOperation
            :description: QtNetwork/QNetworkAccessManager-Operation-PutOperation-v.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetwork/QNetworkAccessManager-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.addStrictTransportSecurityHosts
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QHstsPolicy`]
        :description: QtNetwork/QNetworkAccessManager-addStrictTransportSecurityHosts-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.autoDeleteReplies
        :returns:
            bool
        :description: QtNetwork/QNetworkAccessManager-autoDeleteReplies-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.cache
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractNetworkCache`
        :description: QtNetwork/QNetworkAccessManager-cache-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.clearAccessCache
        :description: QtNetwork/QNetworkAccessManager-clearAccessCache-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.clearConnectionCache
        :description: QtNetwork/QNetworkAccessManager-clearConnectionCache-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.connectToHost
        :args:
            Optional[str]
            port: int = 80
        :description: QtNetwork/QNetworkAccessManager-connectToHost-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.connectToHostEncrypted
        :args:
            Optional[str]
            port: int = 443
            sslConfiguration: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` = QSslConfiguration.defaultConfiguration()
        :description: QtNetwork/QNetworkAccessManager-connectToHostEncrypted-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.connectToHostEncrypted
        :args:
            Optional[str]
            int
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
            Optional[str]
        :description: QtNetwork/QNetworkAccessManager-connectToHostEncrypted-f-3.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.cookieJar
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar`
        :description: QtNetwork/QNetworkAccessManager-cookieJar-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.createRequest
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.Operation`
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            device: :sip:ref:`~PyQt6.QtCore.QIODevice` = None
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-createRequest-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.deleteResource
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-deleteResource-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.enableStrictTransportSecurityStore
        :args:
            bool
            storeDir: Optional[str] = ''
        :description: QtNetwork/QNetworkAccessManager-enableStrictTransportSecurityStore-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.get
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-get-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.get
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-get-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.get
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-get-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.head
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-head-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.isStrictTransportSecurityEnabled
        :returns:
            bool
        :description: QtNetwork/QNetworkAccessManager-isStrictTransportSecurityEnabled-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.isStrictTransportSecurityStoreEnabled
        :returns:
            bool
        :description: QtNetwork/QNetworkAccessManager-isStrictTransportSecurityStoreEnabled-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.post
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-post-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.post
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-post-f-3.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.post
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-post-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.proxy
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtNetwork/QNetworkAccessManager-proxy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.proxyFactory
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory`
        :description: QtNetwork/QNetworkAccessManager-proxyFactory-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.put
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-put-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.put
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-put-f-3.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.put
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-put-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.redirectPolicy
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy`
        :description: QtNetwork/QNetworkAccessManager-redirectPolicy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.sendCustomRequest
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            data: :sip:ref:`~PyQt6.QtCore.QIODevice` = None
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-sendCustomRequest-f-3.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.sendCustomRequest
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-sendCustomRequest-f-4.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.sendCustomRequest
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-sendCustomRequest-f-5.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.setAutoDeleteReplies
        :args:
            bool
        :description: QtNetwork/QNetworkAccessManager-setAutoDeleteReplies-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.setCache
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractNetworkCache`
        :description: QtNetwork/QNetworkAccessManager-setCache-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.setCookieJar
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar`
        :description: QtNetwork/QNetworkAccessManager-setCookieJar-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.setProxy
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtNetwork/QNetworkAccessManager-setProxy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.setProxyFactory
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory`
        :description: QtNetwork/QNetworkAccessManager-setProxyFactory-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.setRedirectPolicy
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy`
        :description: QtNetwork/QNetworkAccessManager-setRedirectPolicy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.setStrictTransportSecurityEnabled
        :args:
            bool
        :description: QtNetwork/QNetworkAccessManager-setStrictTransportSecurityEnabled-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.setTransferTimeout
        :args:
            timeout: int = :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.TransferTimeoutConstant.DefaultTransferTimeoutConstant`
        :description: QtNetwork/QNetworkAccessManager-setTransferTimeout-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.strictTransportSecurityHosts
        :returns:
            list[:sip:ref:`~PyQt6.QtNetwork.QHstsPolicy`]
        :description: QtNetwork/QNetworkAccessManager-strictTransportSecurityHosts-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.supportedSchemes
        :returns:
            list[str]
        :description: QtNetwork/QNetworkAccessManager-supportedSchemes-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.supportedSchemesImplementation
        :returns:
            list[str]
        :description: QtNetwork/QNetworkAccessManager-supportedSchemesImplementation-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkAccessManager.transferTimeout
        :returns:
            int
        :description: QtNetwork/QNetworkAccessManager-transferTimeout-f.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkAccessManager.authenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
            :sip:ref:`~PyQt6.QtNetwork.QAuthenticator`
        :description: QtNetwork/QNetworkAccessManager-authenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkAccessManager.encrypted
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-encrypted-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkAccessManager.finished
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetwork/QNetworkAccessManager-finished-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkAccessManager.preSharedKeyAuthenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
            :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator`
        :description: QtNetwork/QNetworkAccessManager-preSharedKeyAuthenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkAccessManager.proxyAuthenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
            :sip:ref:`~PyQt6.QtNetwork.QAuthenticator`
        :description: QtNetwork/QNetworkAccessManager-proxyAuthenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QNetworkAccessManager.sslErrors
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslError`]
        :description: QtNetwork/QNetworkAccessManager-sslErrors-s.rst
