.. sip:method-description::
    :status: todo
    :pysig: 76b1d76b58b3fa384e0af90fb23670ee
    :realsig: (QBluetooth::SecurityFlags)
    :digest: 2d1fe05700797e9eba383adb65740628

Sets the Bluetooth security flags to *security*. This function must be called before calling :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.listen`. The Bluetooth link will always be encrypted when using Bluetooth 2.1 devices as encryption is mandatory.

Android only supports two levels of security (secure and non-secure). If this flag is set to :sip:ref:`~PyQt6.QtBluetooth.QBluetooth.Security.NoSecurity` the server object will not employ any authentication or encryption. Any other security flag combination will trigger a secure Bluetooth connection.

On macOS, security flags are not supported and will be ignored.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.securityFlags`.
