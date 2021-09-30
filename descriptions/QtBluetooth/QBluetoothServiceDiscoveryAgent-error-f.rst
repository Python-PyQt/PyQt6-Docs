.. sip:method-description::
    :status: todo
    :pysig: b4635a339bcce256d3a813bb1efde9da
    :realsig: () const
    :digest: 00e7e5c44672f63d942bf312394a9b8d

Returns the type of error that last occurred. If the service discovery is done for a single :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.remoteAddress` it will return errors that occurred while trying to discover services on that device. If the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.remoteAddress` is not set and devices are discovered by a scan, errors during service discovery on individual devices are not saved and no signals are emitted. In this case, errors are fairly normal as some devices may not respond to discovery or may no longer be in range. Such errors are surpressed. If no services are returned, it can be assumed no services could be discovered.
