.. sip:method-description::
    :status: todo
    :pysig: 6e862321188e0284d08325e12acf151e
    :realsig: () const
    :digest: 2af5e6cdfacf3d13a305ce0bfdf83ba7

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

**Note:** It is not recommended to use both notifications and indications on the same characteristic. This applies to both server-side when setting up the characteristics, as well as client-side when enabling them. The bluetooth stack behavior differs from platform to platform and the cross-platform behavior will likely be inconsistent. As an example a Bluez Linux client might unconditionally try to enable both mechanisms if both are supported, whereas a macOS client might unconditionally enable just the notifications. If both are needed consider creating two separate characteristics.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.descriptor`.
