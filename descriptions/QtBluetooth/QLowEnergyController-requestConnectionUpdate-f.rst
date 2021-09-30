.. sip:method-description::
    :status: todo
    :pysig: 6763f06f87fc85e4e0e37b1c647e6327
    :realsig: (const QLowEnergyConnectionParameters&)
    :digest: c785f95f42f01fc17990703cf3abcabf

Requests the controller to update the connection according to *parameters*. If the request is successful, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectionUpdated` signal will be emitted with the actual new parameters. See the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters` class for more information on connection parameters.

Android only indirectly permits the adjustment of this parameter set. The connection parameters are separated into three categories (high, low & balanced priority). Each category implies a pre-configured set of values for :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.minimumInterval`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.maximumInterval` and :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.latency`. Although the connection request is an asynchronous operation, Android does not provide a callback stating the result of the request. This is an acknowledged Android bug. Due to this bug Android does not emit the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectionUpdated` signal.

**Note:** Currently, this functionality is only implemented on Linux and Android.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectionUpdated`.
