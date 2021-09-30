.. sip:method-description::
    :status: todo
    :pysig: 6e862321188e0284d08325e12acf151e
    :realsig: () const
    :digest: f30c7a600ecd995f5f835c10c1dc442d

Returns the Client Characteristic Configuration Descriptor or an invalid `QLowEnergyDescriptor <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergydescriptor>`_ instance if no Client Characteristic Configuration Descriptor exists.

BTLE characteristics can support notifications and/or indications. In both cases, the peripheral will inform the central on each change of the characteristic's value. In the BTLE attribute protocol, notification messages are not confirmed by the central, while indications are confirmed. Notifications are considered faster, but unreliable, while indications are slower and more reliable.

If a characteristic supports notification or indication, these can be enabled by writing special bit patterns to the Client Characteristic Configuration Descriptor. For convenience, these bit patterns are provided as QLowEnergyCharacteristic::CCCDDisable, QLowEnergyCharacteristic::CCCDEnableNotification, and QLowEnergyCharacteristic::CCCDEnableIndication.

Enabling e.g. notification for a characteristic named ``mycharacteristic`` in a service called ``myservice`` could be done using the following code.

::

    auto cccd = mycharacteristic.clientCharacteristicConfiguration();
    if (!cccd.isValid()) {
        // your error handling
        return error;
    }
    myservice->writeDescriptor(cccd, QLowEnergyCharacteristic::CCCDEnableNotification);

**Note:** Calling ``characteristic.clientCharacteristicConfiguration()`` is equivalent to calling ``characteristic.descriptor(QBluetoothUuid::DescriptorType::ClientCharacteristicConfiguration)``.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.descriptor`.
