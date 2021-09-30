.. sip:signal-description::
    :status: todo
    :pysig: f5a13b3bac878820b76483c7239f5b8c
    :realsig: (const QBluetoothUuid&)
    :digest: e99b37712abf263f6e47c2beb45b4f60

This signal is emitted each time a new service is discovered. The *newService* parameter contains the UUID of the found service.

This signal can only be emitted if the controller is in the ``CentralRole``.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.discoverServices`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.discoveryFinished`.
