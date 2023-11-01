:orphan:

.. sip:class:: PyQt6.QtBluetooth.QLowEnergyService
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtBluetooth/QLowEnergyService-c.rst

    .. sip:enum:: PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode
        :description: QtBluetooth/QLowEnergyService-DiscoveryMode-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode.FullDiscovery
            :description: QtBluetooth/QLowEnergyService-DiscoveryMode-FullDiscovery-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode.SkipValueDiscovery
            :description: QtBluetooth/QLowEnergyService-DiscoveryMode-SkipValueDiscovery-v.rst

    .. sip:enum:: PyQt6.QtBluetooth.QLowEnergyService.ServiceError
        :description: QtBluetooth/QLowEnergyService-ServiceError-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicReadError
            :description: QtBluetooth/QLowEnergyService-ServiceError-CharacteristicReadError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceError.CharacteristicWriteError
            :description: QtBluetooth/QLowEnergyService-ServiceError-CharacteristicWriteError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceError.DescriptorReadError
            :description: QtBluetooth/QLowEnergyService-ServiceError-DescriptorReadError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceError.DescriptorWriteError
            :description: QtBluetooth/QLowEnergyService-ServiceError-DescriptorWriteError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceError.NoError
            :description: QtBluetooth/QLowEnergyService-ServiceError-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceError.OperationError
            :description: QtBluetooth/QLowEnergyService-ServiceError-OperationError-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceError.UnknownError
            :description: QtBluetooth/QLowEnergyService-ServiceError-UnknownError-v.rst

    .. sip:enum:: PyQt6.QtBluetooth.QLowEnergyService.ServiceState
        :description: QtBluetooth/QLowEnergyService-ServiceState-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceState.DiscoveringService
            :description: QtBluetooth/QLowEnergyService-ServiceState-DiscoveringService-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceState.DiscoveryRequired
            :description: QtBluetooth/QLowEnergyService-ServiceState-DiscoveryRequired-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceState.InvalidService
            :description: QtBluetooth/QLowEnergyService-ServiceState-InvalidService-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceState.LocalService
            :description: QtBluetooth/QLowEnergyService-ServiceState-LocalService-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceState.RemoteService
            :description: QtBluetooth/QLowEnergyService-ServiceState-RemoteService-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceState.RemoteServiceDiscovered
            :description: QtBluetooth/QLowEnergyService-ServiceState-RemoteServiceDiscovered-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceState.RemoteServiceDiscovering
            :description: QtBluetooth/QLowEnergyService-ServiceState-RemoteServiceDiscovering-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceState.ServiceDiscovered
            :description: QtBluetooth/QLowEnergyService-ServiceState-ServiceDiscovered-v.rst

    .. sip:enum:: PyQt6.QtBluetooth.QLowEnergyService.ServiceType
        :description: QtBluetooth/QLowEnergyService-ServiceType-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceType.IncludedService
            :description: QtBluetooth/QLowEnergyService-ServiceType-IncludedService-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.ServiceType.PrimaryService
            :description: QtBluetooth/QLowEnergyService-ServiceType-PrimaryService-v.rst

    .. sip:enum:: PyQt6.QtBluetooth.QLowEnergyService.WriteMode
        :description: QtBluetooth/QLowEnergyService-WriteMode-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.WriteMode.WriteSigned
            :description: QtBluetooth/QLowEnergyService-WriteMode-WriteSigned-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.WriteMode.WriteWithoutResponse
            :description: QtBluetooth/QLowEnergyService-WriteMode-WriteWithoutResponse-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyService.WriteMode.WriteWithResponse
            :description: QtBluetooth/QLowEnergyService-WriteMode-WriteWithResponse-v.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.characteristic
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid`
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`
        :description: QtBluetooth/QLowEnergyService-characteristic-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.characteristics
        :returns:
            List[:sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`]
        :description: QtBluetooth/QLowEnergyService-characteristics-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.contains
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`
        :returns:
            bool
        :description: QtBluetooth/QLowEnergyService-contains-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.contains
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor`
        :returns:
            bool
        :description: QtBluetooth/QLowEnergyService-contains-f-1.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.discoverDetails
        :args:
            mode: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode` = :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode.FullDiscovery`
        :description: QtBluetooth/QLowEnergyService-discoverDetails-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.error
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError`
        :description: QtBluetooth/QLowEnergyService-error-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.includedServices
        :returns:
            List[:sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid`]
        :description: QtBluetooth/QLowEnergyService-includedServices-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.readCharacteristic
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`
        :description: QtBluetooth/QLowEnergyService-readCharacteristic-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.readDescriptor
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor`
        :description: QtBluetooth/QLowEnergyService-readDescriptor-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.serviceName
        :returns:
            str
        :description: QtBluetooth/QLowEnergyService-serviceName-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.serviceUuid
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid`
        :description: QtBluetooth/QLowEnergyService-serviceUuid-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.state
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState`
        :description: QtBluetooth/QLowEnergyService-state-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.type
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceType`
        :description: QtBluetooth/QLowEnergyService-type-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            mode: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.WriteMode` = :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.WriteMode.WriteWithResponse`
        :description: QtBluetooth/QLowEnergyService-writeCharacteristic-f-1.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyService.writeDescriptor
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtBluetooth/QLowEnergyService-writeDescriptor-f-1.rst

    .. sip:signal:: PyQt6.QtBluetooth.QLowEnergyService.characteristicChanged
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtBluetooth/QLowEnergyService-characteristicChanged-s-1.rst

    .. sip:signal:: PyQt6.QtBluetooth.QLowEnergyService.characteristicRead
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtBluetooth/QLowEnergyService-characteristicRead-s-1.rst

    .. sip:signal:: PyQt6.QtBluetooth.QLowEnergyService.characteristicWritten
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtBluetooth/QLowEnergyService-characteristicWritten-s-1.rst

    .. sip:signal:: PyQt6.QtBluetooth.QLowEnergyService.descriptorRead
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtBluetooth/QLowEnergyService-descriptorRead-s-1.rst

    .. sip:signal:: PyQt6.QtBluetooth.QLowEnergyService.descriptorWritten
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtBluetooth/QLowEnergyService-descriptorWritten-s-1.rst

    .. sip:signal:: PyQt6.QtBluetooth.QLowEnergyService.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceError`
        :description: QtBluetooth/QLowEnergyService-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtBluetooth.QLowEnergyService.stateChanged
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState`
        :description: QtBluetooth/QLowEnergyService-stateChanged-s.rst
