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
            :sip:ref:`~PyQt6.QtCore.QByteArray`|bytes|bytearray|memoryview
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-callbackDataReceived-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.callbackReceived
        :args:
            dict[str|None, Any]
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-callbackReceived-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.replyDataReceived
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`|bytes|bytearray|memoryview
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-replyDataReceived-s.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.tokenRequestErrorOccurred
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.Error`
            str|None
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-tokenRequestErrorOccurred-s-1.rst

    .. sip:signal:: PyQt6.QtNetworkAuth.QAbstractOAuthReplyHandler.tokensReceived
        :args:
            dict[str|None, Any]
        :description: QtNetworkAuth/QAbstractOAuthReplyHandler-tokensReceived-s-1.rst
