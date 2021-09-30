.. sip:method-description::
    :status: todo
    :pysig: be0d293965eb640c7242850fa4e6496d
    :realsig: (quint16,const QByteArray&)
    :digest: de5bd2760fd575b02fea9c24ce17b90c

Sets the advertised manufacturer *data* for the given *manufacturerId*. Returns ``true`` if it was inserted, ``false`` if it was already known.

Since Qt 5.14, different values for *data* and the same *manufacturerId* no longer replace each other but are accumulated for the duration of a device scan.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.manufacturerData`.
