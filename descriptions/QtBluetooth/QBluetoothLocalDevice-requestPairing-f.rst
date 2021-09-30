.. sip:method-description::
    :status: todo
    :pysig: d23bef37fada25f2a9b65260d24197bb
    :realsig: (const QBluetoothAddress&,QBluetoothLocalDevice::Pairing)
    :digest: 6a430340906c47a2b45a0d5227a42aa0

Set the *pairing* status with *address*. The results are returned by the signal, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.pairingFinished`. On Android and macOS, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.Pairing.AuthorizedPaired` is not possible and will have the same behavior as Paired.

On macOS, it is not possible to unpair a device. If Unpaired is requested, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.pairingFinished` is immediately emitted although the device remains paired. It is possible to request the pairing for a previously unpaired device. In addition :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.Pairing.AuthorizedPaired` has the same behavior as :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.Pairing.Paired`.

Caution: creating a pairing may take minutes, and may require the user to acknowledge.
