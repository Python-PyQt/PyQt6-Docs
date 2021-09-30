:orphan:

.. sip:class:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-c.rst

    .. sip:enum:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.DiscoveryMethod
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-DiscoveryMethod-e.rst

    .. sip:enum:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-Error-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error.InputOutputError
            :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-Error-InputOutputError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error.InvalidBluetoothAdapterError
            :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-Error-InvalidBluetoothAdapterError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error.LocationServiceTurnedOffError
            :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-Error-LocationServiceTurnedOffError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error.NoError
            :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error.PoweredOffError
            :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-Error-PoweredOffError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error.UnknownError
            :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-Error-UnknownError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error.UnsupportedDiscoveryMethod
            :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-Error-UnsupportedDiscoveryMethod-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error.UnsupportedPlatformError
            :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-Error-UnsupportedPlatformError-v.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-__init__-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.__init__
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-__init__-f-1.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.discoveredDevices
        :returns:
            List[:sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo`]
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-discoveredDevices-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.error
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error`
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-error-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.errorString
        :returns:
            str
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-errorString-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.isActive
        :returns:
            bool
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-isActive-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.lowEnergyDiscoveryTimeout
        :returns:
            int
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-lowEnergyDiscoveryTimeout-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.setLowEnergyDiscoveryTimeout
        :args:
            int
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-setLowEnergyDiscoveryTimeout-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.start
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-start-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.start
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.DiscoveryMethod`
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-start-f-1.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.stop
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-stop-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.supportedDiscoveryMethods
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.DiscoveryMethod`
        :static:
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-supportedDiscoveryMethods-f.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.canceled
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-canceled-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.deviceDiscovered
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo`
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-deviceDiscovered-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.deviceUpdated
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo`
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.Field`
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-deviceUpdated-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error`
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.finished
        :description: QtBluetooth/QBluetoothDeviceDiscoveryAgent-finished-s.rst
