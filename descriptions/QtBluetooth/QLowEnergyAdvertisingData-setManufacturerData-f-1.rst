.. sip:method-description::
    :status: todo
    :pysig: 6506bcc0dc6b9f5bc554559212db4fae
    :realsig: (quint16, const QByteArray&)
    :digest: 878ce30a45a46c0820dc856162e9f1a1

Sets the manufacturer id and data. The *id* parameter is a company identifier as assigned by the Bluetooth SIG. The *data* parameter is an arbitrary value.

**Note:** macOS and iOS do not support advertising of manufacturer id or data, so the provided parameters will be ignored on these platforms.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingData.manufacturerData`.
