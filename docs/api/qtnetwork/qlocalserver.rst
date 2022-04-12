:orphan:

.. sip:class:: PyQt6.QtNetwork.QLocalServer
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtNetwork/QLocalServer-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QLocalServer.SocketOption
        :description: QtNetwork/QLocalServer-SocketOption-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QLocalServer.SocketOption.AbstractNamespaceOption
            :description: QtNetwork/QLocalServer-SocketOption-AbstractNamespaceOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QLocalServer.SocketOption.GroupAccessOption
            :description: QtNetwork/QLocalServer-SocketOption-GroupAccessOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QLocalServer.SocketOption.OtherAccessOption
            :description: QtNetwork/QLocalServer-SocketOption-OtherAccessOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QLocalServer.SocketOption.UserAccessOption
            :description: QtNetwork/QLocalServer-SocketOption-UserAccessOption-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QLocalServer.SocketOption.WorldAccessOption
            :description: QtNetwork/QLocalServer-SocketOption-WorldAccessOption-v.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetwork/QLocalServer-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.close
        :description: QtNetwork/QLocalServer-close-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.errorString
        :returns:
            str
        :description: QtNetwork/QLocalServer-errorString-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.fullServerName
        :returns:
            str
        :description: QtNetwork/QLocalServer-fullServerName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.hasPendingConnections
        :returns:
            bool
        :description: QtNetwork/QLocalServer-hasPendingConnections-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.incomingConnection
        :args:
            PyQt6.sip.voidptr
        :description: QtNetwork/QLocalServer-incomingConnection-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.isListening
        :returns:
            bool
        :description: QtNetwork/QLocalServer-isListening-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.listen
        :args:
            str
        :returns:
            bool
        :description: QtNetwork/QLocalServer-listen-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.listen
        :args:
            PyQt6.sip.voidptr
        :returns:
            bool
        :description: QtNetwork/QLocalServer-listen-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.listenBacklogSize
        :returns:
            int
        :description: QtNetwork/QLocalServer-listenBacklogSize-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.maxPendingConnections
        :returns:
            int
        :description: QtNetwork/QLocalServer-maxPendingConnections-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.nextPendingConnection
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QLocalSocket`
        :description: QtNetwork/QLocalServer-nextPendingConnection-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.removeServer
        :args:
            str
        :returns:
            bool
        :static:
        :description: QtNetwork/QLocalServer-removeServer-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.serverError
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtNetwork/QLocalServer-serverError-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.serverName
        :returns:
            str
        :description: QtNetwork/QLocalServer-serverName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.setListenBacklogSize
        :args:
            int
        :description: QtNetwork/QLocalServer-setListenBacklogSize-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.setMaxPendingConnections
        :args:
            int
        :description: QtNetwork/QLocalServer-setMaxPendingConnections-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.setSocketOptions
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QLocalServer.SocketOption`
        :description: QtNetwork/QLocalServer-setSocketOptions-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.socketDescriptor
        :returns:
            PyQt6.sip.voidptr
        :description: QtNetwork/QLocalServer-socketDescriptor-f.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.socketOptions
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QLocalServer.SocketOption`
        :description: QtNetwork/QLocalServer-socketOptions-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QLocalServer.waitForNewConnection
        :args:
            msecs: int = 0
        :returns:
            bool
            bool
        :description: QtNetwork/QLocalServer-waitForNewConnection-f.rst

    .. sip:signal:: PyQt6.QtNetwork.QLocalServer.newConnection
        :description: QtNetwork/QLocalServer-newConnection-s.rst
