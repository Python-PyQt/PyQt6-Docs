.. sip:method-description::
    :status: todo
    :pysig: b7bdcad4251b549a6c0169e723ade14f
    :realsig: (QLowEnergyAdvertisingData::Discoverability)
    :digest: e4f8b952b1c902823153875823d45b90

Sets the discoverability type of the advertising device to *mode*.

**Note:** Discoverability information can only appear in an actual advertising data packet. If this object acts as scan response data, a call to this function will have no effect on the scan response sent.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingData.discoverability`.
