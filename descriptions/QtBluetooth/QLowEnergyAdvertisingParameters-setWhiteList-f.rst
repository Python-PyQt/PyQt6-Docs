.. sip:method-description::
    :status: todo
    :pysig: 3bd5c0b92010703df033e6e193968ae2
    :realsig: (const QList<QLowEnergyAdvertisingParameters::AddressInfo>&,QLowEnergyAdvertisingParameters::FilterPolicy)
    :digest: 3d80f1f66f425804d74b681b045066ef

Sets the white list that is potentially used for filtering scan and connection requests. The *whiteList* parameter is the list of addresses to use for filtering, and *policy* specifies how exactly to use *whiteList*.

Whitelists are not supported on the BlueZ DBus backend as they are not supported by BlueZ.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingParameters.whiteList`.
