.. sip:method-description::
    :status: todo
    :pysig: ae0dec1c3252a134c07d21940b79d2ed
    :realsig: (const QLowEnergyServiceData&,QObject*)
    :digest: b7e9d9d66159b7b2a30589b044a2e320

Constructs and returns a `QLowEnergyService <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergyservice>`_ object with *parent* from *service*. The controller must be in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole` and in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.ControllerState.UnconnectedState`. The *service* object must be valid.

**Note:** Once the peripheral instance is disconnected from the remote central device or if :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.disconnectFromDevice` is manually called, every service definition that was previously added via this function is removed from the peripheral. Therefore this function must be called again before re-advertising this peripheral controller instance. The described behavior is connection specific and therefore not dependent on whether :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.stopAdvertising` was called.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.stopAdvertising`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.disconnectFromDevice`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyServiceData.addIncludedService`.
