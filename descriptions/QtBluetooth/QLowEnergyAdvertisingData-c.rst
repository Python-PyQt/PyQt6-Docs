.. sip:class-description::
    :status: todo
    :brief: Represents the data to be broadcast during Bluetooth Low Energy advertising
    :digest: 601cf6ec5cea13048278e68705394e1a

The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingData` class represents the data to be broadcast during Bluetooth Low Energy advertising.

This data can include the device name, GATT services offered by the device, and so on. The data set via this class will be used when advertising is started by calling :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.startAdvertising`. Objects of this class can represent an Advertising Data packet or a Scan Response packet.

.. _qlowenergyadvertisingdata-advertising-data-limitations:

Advertising Data Limitations
............................

The maximum length of the advertisement data depends on the bluetooth device and the platform bluetooth stack. For maximum compatibility, it is recommended to limit the advertising data size to the legacy advertising limit of 31 bytes.

If the variable-length data set via this class exceeds the supported limit, the behavior will depend on the underlying Bluetooth stack implementation. The most typical possibilities are:

* the extra data can be truncated or entirely left out;

* the advertising fails to start.

For example, on Android, advertising will fail if the advertising data is larger than 31 bytes. On BlueZ DBus backend, the advertising length limit and the behavior when it is exceeded is up to BlueZ; it may, for example support extended advertising, or may fail to start the advertising.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingParameters`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.startAdvertising`.
