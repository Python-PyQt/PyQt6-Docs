.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: f803f87f71e12c69b53ab21996ba507e

Connects to the remote Bluetooth Low Energy device.

This function does nothing if the controller's :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.state` is not equal to :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.ControllerState.UnconnectedState`. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connected` signal is emitted once the connection is successfully established.

On Linux/BlueZ systems, it is not possible to connect to the same remote device using two instances of this class. The second call to this function may fail with an error. This limitation may be removed in future releases.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.disconnectFromDevice`.
