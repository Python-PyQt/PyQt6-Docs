:orphan:

.. sip:class:: PyQt6.QtNetwork.QTcpServer
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtNetwork/QTcpServer-c.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetwork/QTcpServer-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.addPendingConnection
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`
        :description: QtNetwork/QTcpServer-addPendingConnection-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.close
        :description: QtNetwork/QTcpServer-close-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.errorString
        :returns:
            str
        :description: QtNetwork/QTcpServer-errorString-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.hasPendingConnections
        :returns:
            bool
        :description: QtNetwork/QTcpServer-hasPendingConnections-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.incomingConnection
        :args:
            PyQt6.sip.voidptr
        :description: QtNetwork/QTcpServer-incomingConnection-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.isListening
        :returns:
            bool
        :description: QtNetwork/QTcpServer-isListening-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.listen
        :args:
            address: Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`] = :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.Any`
            port: int = 0
        :returns:
            bool
        :description: QtNetwork/QTcpServer-listen-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.listenBacklogSize
        :returns:
            int
        :description: QtNetwork/QTcpServer-listenBacklogSize-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.maxPendingConnections
        :returns:
            int
        :description: QtNetwork/QTcpServer-maxPendingConnections-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.nextPendingConnection
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`
        :description: QtNetwork/QTcpServer-nextPendingConnection-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.pauseAccepting
        :description: QtNetwork/QTcpServer-pauseAccepting-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.proxy
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtNetwork/QTcpServer-proxy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.resumeAccepting
        :description: QtNetwork/QTcpServer-resumeAccepting-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.serverAddress
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtNetwork/QTcpServer-serverAddress-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.serverError
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtNetwork/QTcpServer-serverError-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.serverPort
        :returns:
            int
        :description: QtNetwork/QTcpServer-serverPort-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.setListenBacklogSize
        :args:
            int
        :description: QtNetwork/QTcpServer-setListenBacklogSize-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.setMaxPendingConnections
        :args:
            int
        :description: QtNetwork/QTcpServer-setMaxPendingConnections-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.setProxy
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`
        :description: QtNetwork/QTcpServer-setProxy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.setSocketDescriptor
        :args:
            PyQt6.sip.voidptr
        :returns:
            bool
        :description: QtNetwork/QTcpServer-setSocketDescriptor-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.socketDescriptor
        :returns:
            PyQt6.sip.voidptr
        :description: QtNetwork/QTcpServer-socketDescriptor-f.rst

    .. sip:method:: PyQt6.QtNetwork.QTcpServer.waitForNewConnection
        :args:
            msecs: int = 0
        :returns:
            bool
            bool
        :description: QtNetwork/QTcpServer-waitForNewConnection-f.rst

    .. sip:signal:: PyQt6.QtNetwork.QTcpServer.acceptError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtNetwork/QTcpServer-acceptError-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QTcpServer.newConnection
        :description: QtNetwork/QTcpServer-newConnection-s.rst
