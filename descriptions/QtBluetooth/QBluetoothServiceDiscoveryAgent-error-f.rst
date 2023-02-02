.. sip:method-description::
    :status: todo
    :pysig: b4635a339bcce256d3a813bb1efde9da
    :realsig: () const
    :digest: 5c9809f6fc602f781a97934ca257188e

Returns the type of error that last occurred. If the service discovery is done for a single :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.remoteAddress` it will return errors that occurred while trying to discover services on that device. If the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.remoteAddress` is not set and devices are discovered by a scan, errors during service discovery on individual devices are not saved and no signals are emitted. In this case, errors are fairly normal as some devices may not respond to discovery or may no longer be in range. Such errors are suppressed. If no services are returned, it can be assumed no services could be discovered.

Any possible previous errors are cleared upon restarting the discovery.
