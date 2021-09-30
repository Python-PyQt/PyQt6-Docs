.. sip:signal-description::
    :status: todo
    :pysig: d23bef37fada25f2a9b65260d24197bb
    :realsig: (const QBluetoothAddress&,QBluetoothLocalDevice::Pairing)
    :digest: a36d07763f0f06a8dd9e6ace0622a5e0

Pairing or unpairing has completed with *address*. Current pairing status is in *pairing*. If the pairing request was not successful, this signal will not be emitted. The :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.errorOccurred` signal is emitted if the pairing request failed. The signal is only ever emitted for pairing requests which have previously requested by calling :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.requestPairing` of the current object instance.
