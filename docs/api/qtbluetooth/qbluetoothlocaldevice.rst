:orphan:

.. sip:class:: PyQt6.QtBluetooth.QBluetoothLocalDevice
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtBluetooth/QBluetoothLocalDevice-c.rst

    .. sip:enum:: PyQt6.QtBluetooth.QBluetoothLocalDevice.Error
        :description: QtBluetooth/QBluetoothLocalDevice-Error-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothLocalDevice.Error.NoError
            :description: QtBluetooth/QBluetoothLocalDevice-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothLocalDevice.Error.PairingError
            :description: QtBluetooth/QBluetoothLocalDevice-Error-PairingError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothLocalDevice.Error.UnknownError
            :description: QtBluetooth/QBluetoothLocalDevice-Error-UnknownError-v.rst

    .. sip:enum:: PyQt6.QtBluetooth.QBluetoothLocalDevice.HostMode
        :description: QtBluetooth/QBluetoothLocalDevice-HostMode-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothLocalDevice.HostMode.HostConnectable
            :description: QtBluetooth/QBluetoothLocalDevice-HostMode-HostConnectable-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothLocalDevice.HostMode.HostDiscoverable
            :description: QtBluetooth/QBluetoothLocalDevice-HostMode-HostDiscoverable-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothLocalDevice.HostMode.HostDiscoverableLimitedInquiry
            :description: QtBluetooth/QBluetoothLocalDevice-HostMode-HostDiscoverableLimitedInquiry-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothLocalDevice.HostMode.HostPoweredOff
            :description: QtBluetooth/QBluetoothLocalDevice-HostMode-HostPoweredOff-v.rst

    .. sip:enum:: PyQt6.QtBluetooth.QBluetoothLocalDevice.Pairing
        :description: QtBluetooth/QBluetoothLocalDevice-Pairing-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothLocalDevice.Pairing.AuthorizedPaired
            :description: QtBluetooth/QBluetoothLocalDevice-Pairing-AuthorizedPaired-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothLocalDevice.Pairing.Paired
            :description: QtBluetooth/QBluetoothLocalDevice-Pairing-Paired-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QBluetoothLocalDevice.Pairing.Unpaired
            :description: QtBluetooth/QBluetoothLocalDevice-Pairing-Unpaired-v.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtBluetooth/QBluetoothLocalDevice-__init__-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.__init__
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtBluetooth/QBluetoothLocalDevice-__init__-f-1.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.address
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
        :description: QtBluetooth/QBluetoothLocalDevice-address-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.allDevices
        :returns:
            List[:sip:ref:`~PyQt6.QtBluetooth.QBluetoothHostInfo`]
        :static:
        :description: QtBluetooth/QBluetoothLocalDevice-allDevices-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.connectedDevices
        :returns:
            List[:sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`]
        :description: QtBluetooth/QBluetoothLocalDevice-connectedDevices-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.hostMode
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.HostMode`
        :description: QtBluetooth/QBluetoothLocalDevice-hostMode-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.isValid
        :returns:
            bool
        :description: QtBluetooth/QBluetoothLocalDevice-isValid-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.name
        :returns:
            str
        :description: QtBluetooth/QBluetoothLocalDevice-name-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.pairingStatus
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.Pairing`
        :description: QtBluetooth/QBluetoothLocalDevice-pairingStatus-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.powerOn
        :description: QtBluetooth/QBluetoothLocalDevice-powerOn-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.requestPairing
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.Pairing`
        :description: QtBluetooth/QBluetoothLocalDevice-requestPairing-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QBluetoothLocalDevice.setHostMode
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.HostMode`
        :description: QtBluetooth/QBluetoothLocalDevice-setHostMode-f.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothLocalDevice.deviceConnected
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
        :description: QtBluetooth/QBluetoothLocalDevice-deviceConnected-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothLocalDevice.deviceDisconnected
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
        :description: QtBluetooth/QBluetoothLocalDevice-deviceDisconnected-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothLocalDevice.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.Error`
        :description: QtBluetooth/QBluetoothLocalDevice-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothLocalDevice.hostModeStateChanged
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.HostMode`
        :description: QtBluetooth/QBluetoothLocalDevice-hostModeStateChanged-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QBluetoothLocalDevice.pairingFinished
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress`
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.Pairing`
        :description: QtBluetooth/QBluetoothLocalDevice-pairingFinished-s.rst
