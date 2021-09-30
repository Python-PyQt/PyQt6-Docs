:orphan:

.. sip:class:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-c.rst

    .. sip:enum:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.DiscoveryMode
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-DiscoveryMode-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.DiscoveryMode.FullDiscovery
            :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-DiscoveryMode-FullDiscovery-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.DiscoveryMode.MinimalDiscovery
            :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-DiscoveryMode-MinimalDiscovery-v.rst

    .. sip:enum:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-Error-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error.InputOutputError
            :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-Error-InputOutputError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error.InvalidBluetoothAdapterError
            :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-Error-InvalidBluetoothAdapterError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error.NoError
            :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error.PoweredOffError
            :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-Error-PoweredOffError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error.UnknownError
            :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-Error-UnknownError-v.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-__init__-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.__init__
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-__init__-f-1.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.clear
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-clear-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.discoveredServices
        :returns:
            List[:sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo`]
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-discoveredServices-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.error
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error`
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-error-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.errorString
        :returns:
            str
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-errorString-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.isActive
        :returns:
            bool
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-isActive-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.remoteAddress
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-remoteAddress-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.setRemoteAddress
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
        :returns:
            bool
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-setRemoteAddress-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.setUuidFilter
        :args:
            Iterable[:sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid`]
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-setUuidFilter-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.setUuidFilter
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid`
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-setUuidFilter-f-1.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.start
        :args:
            mode: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.DiscoveryMode` = :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.DiscoveryMode.MinimalDiscovery`
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-start-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.stop
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-stop-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.uuidFilter
        :returns:
            List[:sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid`]
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-uuidFilter-f.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.canceled
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-canceled-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error`
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.finished
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-finished-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.serviceDiscovered
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo`
        :description: QtBluetooth/QBluetoothServiceDiscoveryAgent-serviceDiscovered-s.rst
