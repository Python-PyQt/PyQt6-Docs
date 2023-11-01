:orphan:

.. sip:class:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtNetworkAuth/QAbstractOAuthReplyHandler-c.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-__init__-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.callback
        :returns:
            str
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-callback-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.networkReplyFinished
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-networkReplyFinished-f.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.callbackDataReceived
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-callbackDataReceived-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.callbackReceived
        :args:
            Dict[Optional[str], Any]
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-callbackReceived-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.replyDataReceived
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-replyDataReceived-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.tokenRequestErrorOccurred
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Error`
            Optional[str]
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-tokenRequestErrorOccurred-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.tokensReceived
        :args:
            Dict[Optional[str], Any]
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-tokensReceived-s-1.rst
