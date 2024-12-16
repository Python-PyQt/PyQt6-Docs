:orphan:

.. sip:class:: PyQt6.QtBluetooth.QLowEnergyCharacteristic
    :description: QtBluetooth/QLowEnergyCharacteristic-c.rst

    .. sip:enum:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType
        :description: QtBluetooth/QLowEnergyCharacteristic-PropertyType-e.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Broadcasting
            :description: QtBluetooth/QLowEnergyCharacteristic-PropertyType-Broadcasting-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.ExtendedProperty
            :description: QtBluetooth/QLowEnergyCharacteristic-PropertyType-ExtendedProperty-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Indicate
            :description: QtBluetooth/QLowEnergyCharacteristic-PropertyType-Indicate-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Notify
            :description: QtBluetooth/QLowEnergyCharacteristic-PropertyType-Notify-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Read
            :description: QtBluetooth/QLowEnergyCharacteristic-PropertyType-Read-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Unknown
            :description: QtBluetooth/QLowEnergyCharacteristic-PropertyType-Unknown-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Write
            :description: QtBluetooth/QLowEnergyCharacteristic-PropertyType-Write-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.WriteNoResponse
            :description: QtBluetooth/QLowEnergyCharacteristic-PropertyType-WriteNoResponse-v.rst

        .. sip:enum-member:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.WriteSigned
            :description: QtBluetooth/QLowEnergyCharacteristic-PropertyType-WriteSigned-v.rst

    .. sip:attribute:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.CCCDDisable
        :type: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :const:
        :static:
        :description: QtBluetooth/QLowEnergyCharacteristic-CCCDDisable-a.rst

    .. sip:attribute:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.CCCDEnableIndication
        :type: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :const:
        :static:
        :description: QtBluetooth/QLowEnergyCharacteristic-CCCDEnableIndication-a.rst

    .. sip:attribute:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.CCCDEnableNotification
        :type: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :const:
        :static:
        :description: QtBluetooth/QLowEnergyCharacteristic-CCCDEnableNotification-a.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.__init__
        :description: QtBluetooth/QLowEnergyCharacteristic-__init__-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.__init__
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`
        :description: QtBluetooth/QLowEnergyCharacteristic-__init__-f-1.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.clientCharacteristicConfiguration
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor`
        :description: QtBluetooth/QLowEnergyCharacteristic-clientCharacteristicConfiguration-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.descriptor
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid`
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor`
        :description: QtBluetooth/QLowEnergyCharacteristic-descriptor-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.descriptors
        :returns:
            list[:sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor`]
        :description: QtBluetooth/QLowEnergyCharacteristic-descriptors-f-1.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.__eq__
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`
        :returns:
            bool
        :description: QtBluetooth/QLowEnergyCharacteristic-__eq__-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.isValid
        :returns:
            bool
        :description: QtBluetooth/QLowEnergyCharacteristic-isValid-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.name
        :returns:
            str
        :description: QtBluetooth/QLowEnergyCharacteristic-name-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.__ne__
        :args:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic`
        :returns:
            bool
        :description: QtBluetooth/QLowEnergyCharacteristic-__ne__-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.properties
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType`
        :description: QtBluetooth/QLowEnergyCharacteristic-properties-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.uuid
        :returns:
            :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid`
        :description: QtBluetooth/QLowEnergyCharacteristic-uuid-f.rst

    .. sip:method:: PyQt6.QtBluetooth.QLowEnergyCharacteristic.value
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtBluetooth/QLowEnergyCharacteristic-value-f.rst
