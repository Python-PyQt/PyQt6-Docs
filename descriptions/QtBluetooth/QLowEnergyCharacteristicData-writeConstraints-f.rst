.. sip:method-description::
    :status: todo
    :pysig: 27de13fde32fa0db491a759670b36bfc
    :realsig: () const
    :digest: 0388f1546c425efb58f777d2f1786fb9

Returns the constraints needed for a client to write the value of this characteristic. If :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristicData.properties` does not include either of :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Write`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.WriteNoResponse` and :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.WriteSigned`, this value is irrelevant. By default, there are no write constraints.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristicData.setWriteConstraints`.
