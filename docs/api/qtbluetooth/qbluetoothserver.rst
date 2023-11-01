:orphan:

.. sip:class:: PyQt6.QtBluetooth.QBluetoothServer
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtBluetooth/QBluetoothServer-c.rst

    .. sip:enum:: PyQt6.QtBluetooth.QBluetoothServer.Error
        :description: QtBluetooth/QBluetoothServer-Error-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServer.Error.InputOutputError
            :description: QtBluetooth/QBluetoothServer-Error-InputOutputError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServer.Error.MissingPermissionsError
            :description: QtBluetooth/QBluetoothServer-Error-MissingPermissionsError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServer.Error.NoError
            :description: QtBluetooth/QBluetoothServer-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServer.Error.PoweredOffError
            :description: QtBluetooth/QBluetoothServer-Error-PoweredOffError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServer.Error.ServiceAlreadyRegisteredError
            :description: QtBluetooth/QBluetoothServer-Error-ServiceAlreadyRegisteredError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServer.Error.UnknownError
            :description: QtBluetooth/QBluetoothServer-Error-UnknownError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServer.Error.UnsupportedProtocolError
            :description: QtBluetooth/QBluetoothServer-Error-UnsupportedProtocolError-v.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.__init__
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.Protocol`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtBluetooth/QBluetoothServer-__init__-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.close
        :description: QtBluetooth/QBluetoothServer-close-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.error
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.Error`
        :description: QtBluetooth/QBluetoothServer-error-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.hasPendingConnections
        :returns:
            bool
        :description: QtBluetooth/QBluetoothServer-hasPendingConnections-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.isListening
        :returns:
            bool
        :description: QtBluetooth/QBluetoothServer-isListening-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.listen
        :args:
            address: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress` = QBluetoothAddress()
            port: int = 0
        :returns:
            bool
        :description: QtBluetooth/QBluetoothServer-listen-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.listen
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid`
            serviceName: Optional[str] = ''
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo`
        :description: QtBluetooth/QBluetoothServer-listen-f-2.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.maxPendingConnections
        :returns:
            int
        :description: QtBluetooth/QBluetoothServer-maxPendingConnections-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.nextPendingConnection
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket`
        :description: QtBluetooth/QBluetoothServer-nextPendingConnection-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.securityFlags
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetooth.Security`
        :description: QtBluetooth/QBluetoothServer-securityFlags-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.serverAddress
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
        :description: QtBluetooth/QBluetoothServer-serverAddress-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.serverPort
        :returns:
            int
        :description: QtBluetooth/QBluetoothServer-serverPort-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.serverType
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.Protocol`
        :description: QtBluetooth/QBluetoothServer-serverType-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.setMaxPendingConnections
        :args:
            int
        :description: QtBluetooth/QBluetoothServer-setMaxPendingConnections-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServer.setSecurityFlags
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetooth.Security`
        :description: QtBluetooth/QBluetoothServer-setSecurityFlags-f.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothServer.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.Error`
        :description: QtBluetooth/QBluetoothServer-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothServer.newConnection
        :description: QtBluetooth/QBluetoothServer-newConnection-s.rst
