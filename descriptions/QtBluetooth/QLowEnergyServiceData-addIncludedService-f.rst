.. sip:method-description::
    :status: todo
    :pysig: de324369113bef17e9ec03b17e7efe15
    :realsig: (QLowEnergyService*)
    :digest: e2382cafa610e666a5939f04e69371f8

Adds *service* to the list of included services. The *service* object must have been returned from a call to :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.addService`. This requirement prevents circular includes (which are forbidden by the Bluetooth specification), and also helps to support the use case of including more than one service of the same type.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyServiceData.setIncludedServices`.
