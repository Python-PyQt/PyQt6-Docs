.. sip:method-description::
    :status: todo
    :pysig: 27de13fde32fa0db491a759670b36bfc
    :realsig: () const
    :digest: 85750a7635c9f0fd908cf3860eb2fca1

Returns the constraints needed for a client to read the value of this characteristic. If :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristicData.properties` does not include :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Read`, this value is irrelevant. By default, there are no read constraints.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristicData.setReadConstraints`.
