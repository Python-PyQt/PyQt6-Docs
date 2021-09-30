.. sip:method-description::
    :status: todo
    :pysig: 61c499debf53f80042b09b7c3a199a93
    :realsig: () const
    :digest: 024ec98ca27bdce0659f0ca6295366cd

Returns the type of the service.

**Note:** The type attribute cannot be relied upon until the service has reached the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.ServiceDiscovered` state. This field is initialised with :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceType.PrimaryService`.

**Note:** On Android, it is not possible to determine whether a service is a primary or secondary service. Therefore all services have the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceType.PrimaryService` flag set.
