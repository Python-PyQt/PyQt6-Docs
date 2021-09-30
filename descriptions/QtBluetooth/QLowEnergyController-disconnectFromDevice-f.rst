.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 213500c96956d1886a59853d223912ef

Disconnects from the remote device.

Any `QLowEnergyService <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergyservice>`_, `QLowEnergyCharacteristic <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycharacteristic>`_ or `QLowEnergyDescriptor <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergydescriptor>`_ instance that resulted from the current connection is automatically invalidated. Once any of those objects become invalid they remain invalid even if this controller object reconnects.

This function does nothing if the controller is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.ControllerState.UnconnectedState`.

If the controller is in the peripheral role, it stops advertising and removes all services which have previously been added via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.addService`. To reuse the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController` instance the application must re-add services and restart the advertising mode by calling :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.startAdvertising`.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectToDevice`.
