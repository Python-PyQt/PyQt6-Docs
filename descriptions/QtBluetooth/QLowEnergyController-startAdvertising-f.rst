.. sip:method-description::
    :status: todo
    :pysig: c85a036cd3cb786f8a0a070f688dd14b
    :realsig: (const QLowEnergyAdvertisingParameters&,const QLowEnergyAdvertisingData&,const QLowEnergyAdvertisingData&)
    :digest: af43513f38dc2e01bf96ae2be222bc30

Starts advertising the data given in *advertisingData* and *scanResponseData*, using the parameters set in *parameters*. The controller has to be in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole`. If *parameters* indicates that the advertisement should be connectable, then this function also starts listening for incoming client connections.

Providing *scanResponseData* is not required, as it is not applicable for certain configurations of ``parameters``. *advertisingData* and *scanResponseData* are limited to 31 byte user data. If, for example, several 128bit uuids are added to *advertisingData*, the advertised packets may not contain all uuids. The existing limit may have caused the truncation of uuids. In such cases *scanResponseData* may be used for additional information.

If this object is currently not in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.ControllerState.UnconnectedState`, nothing happens.

**Note:** Advertising will stop automatically once a client connects to the local device.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.stopAdvertising`.
