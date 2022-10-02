:orphan:

.. sip:class:: PyQt6.QtNetwork.QSslServer
    :inherits: :sip:ref:`~PyQt6.QtNetwork.QTcpServer`
    :description: QtNetwork/QSslServer-c.rst

    .. sip:method:: PyQt6.QtNetwork.QSslServer.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetwork/QSslServer-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslServer.handshakeTimeout
        :returns:
            int
        :description: QtNetwork/QSslServer-handshakeTimeout-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslServer.incomingConnection
        :args:
            PyQt6.sip.voidptr
        :description: QtNetwork/QSslServer-incomingConnection-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslServer.setHandshakeTimeout
        :args:
            int
        :description: QtNetwork/QSslServer-setHandshakeTimeout-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslServer.setSslConfiguration
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtNetwork/QSslServer-setSslConfiguration-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslServer.sslConfiguration
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`
        :description: QtNetwork/QSslServer-sslConfiguration-f.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslServer.alertReceived
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket`
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertLevel`
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertType`
            str
        :description: QtNetwork/QSslServer-alertReceived-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslServer.alertSent
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket`
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertLevel`
            :sip:ref:`~PyQt6.QtNetwork.QSsl.AlertType`
            str
        :description: QtNetwork/QSslServer-alertSent-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslServer.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket`
            :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError`
        :description: QtNetwork/QSslServer-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslServer.handshakeInterruptedOnError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket`
            :sip:ref:`~PyQt6.QtNetwork.QSslError`
        :description: QtNetwork/QSslServer-handshakeInterruptedOnError-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslServer.peerVerifyError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket`
            :sip:ref:`~PyQt6.QtNetwork.QSslError`
        :description: QtNetwork/QSslServer-peerVerifyError-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslServer.preSharedKeyAuthenticationRequired
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket`
            :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator`
        :description: QtNetwork/QSslServer-preSharedKeyAuthenticationRequired-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslServer.sslErrors
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket`
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslError`]
        :description: QtNetwork/QSslServer-sslErrors-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QSslServer.startedEncryptionHandshake
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslSocket`
        :description: QtNetwork/QSslServer-startedEncryptionHandshake-s.rst
