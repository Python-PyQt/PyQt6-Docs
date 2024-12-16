.. sip:method-description::
    :status: todo
    :pysig: bbf27f882023364b890a3a27242c8c12
    :realsig: () const
    :digest: 63dc6525cf67dbe04f8c1264a0836797

Returns the UUIDs of all services which are included by the current service.

The returned list is empty if this service instance's :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.discoverDetails` was not yet called or there are no known characteristics.

It is possible that an included service contains yet another service. Such second level includes have to be obtained via their relevant first level :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService` instance. Technically, this could create a circular dependency.

:sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.createServiceObject` should be used to obtain service instances for each of the UUIDs.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.createServiceObject`.
