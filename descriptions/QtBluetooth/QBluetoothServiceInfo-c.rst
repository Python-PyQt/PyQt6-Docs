.. sip:class-description::
    :status: todo
    :brief: Enables access to the attributes of a Bluetooth service
    :digest: cb6238a86230e5ecdc2488d023bffe98

The :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo` class enables access to the attributes of a Bluetooth service.

:sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo` provides information about a service offered by a Bluetooth device. In addition it can be used to register new services on the local device. Note that such a registration only affects the Bluetooth SDP entries. Any server listening for incoming connections (e.g an RFCOMM server) must be started before :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.registerService` is called. Deregistration must happen in the reverse order.

:sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo` is not a value type in the traditional sense. All copies of the same service info object share the same data as they do not detach upon changing them. This ensures that two copies can (de)register the same Bluetooth service.

On iOS, this class cannot be used because the platform does not expose an API which may permit access to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo` related features.
