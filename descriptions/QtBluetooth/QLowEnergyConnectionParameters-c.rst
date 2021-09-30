.. sip:class-description::
    :status: todo
    :brief: Used when requesting or reporting an update of the parameters of a Bluetooth LE connection
    :digest: 3a71d1cf57a2d04ab076227f109055e3

The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters` class is used when requesting or reporting an update of the parameters of a Bluetooth LE connection.

The connection parameters influence how often a master and a slave device synchronize with each other. In general, a lower connection interval and latency means faster communication, but also higher power consumption. How these criteria should be weighed against each other is highly dependent on the concrete use case.

Android only indirectly permits the adjustment of this parameter set. The platform separates the connection parameters into three categories (hight, low & balanced priority). Each category implies a predefined set of values for :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.minimumInterval`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.maximumInterval` and :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.latency`. Additionally, the value ranges of each category can vary from one Android device to the next. Qt uses the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.minimumInterval` to determine the target category as follows:

+------------------------------------------------------------------------------+-------------------------------+
| :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.minimumInterval` | Android priority              |
+==============================================================================+===============================+
| interval < 30                                                                | CONNECTION_PRIORITY_HIGH      |
+------------------------------------------------------------------------------+-------------------------------+
| 30 <= interval <= 100                                                        | CONNECTION_PRIORITY_BALANCED  |
+------------------------------------------------------------------------------+-------------------------------+
| interval > 100                                                               | CONNECTION_PRIORITY_LOW_POWER |
+------------------------------------------------------------------------------+-------------------------------+

The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.supervisionTimeout` cannot be changed on Android and is therefore ignored.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.requestConnectionUpdate`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectionUpdated`.
