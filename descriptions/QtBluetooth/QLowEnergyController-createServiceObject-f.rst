.. sip:method-description::
    :status: todo
    :pysig: d4439368e46ced80447411407cc97eb4
    :realsig: (const QBluetoothUuid&,QObject*)
    :digest: 69b93472c4a73407689740381b2a2cba

Creates an instance of the service represented by *serviceUuid*. The *serviceUuid* parameter must have been obtained via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.services`.

The caller takes ownership of the returned pointer and may pass a *parent* parameter as default owner.

This function returns a null pointer if no service with *serviceUuid* can be found on the remote device or the controller is disconnected.

This function can return instances for secondary services too. The include relationships between services can be expressed via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.includedServices`.

If this function is called multiple times using the same service UUID, the returned `QLowEnergyService <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergyservice>`_ instances share their internal data. Therefore if one of the instances initiates the discovery of the service details, the other instances automatically transition into the discovery state too.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.services`.
