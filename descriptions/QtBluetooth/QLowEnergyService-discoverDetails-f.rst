.. sip:method-description::
    :status: todo
    :pysig: a98f4ab2cbf5d2c5a0d6ba633f9c708d
    :realsig: (QLowEnergyService::DiscoveryMode)
    :digest: e80363df25f8648e10b4eeaa39ad1ea5

Initiates discovery of the service's included services, characteristics, and their associated descriptors.

The discovery process is indicated via the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.stateChanged` signal. After creation, the service is in :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.DiscoveryRequired` state. When calling  it transitions to :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.DiscoveringService`. After completion of detail discovery, it transitions to :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.ServiceState.ServiceDiscovered` state. On each transition, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.stateChanged` signal is emitted. Depending on the argument *mode*, a :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode.FullDiscovery` or a :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode.SkipValueDiscovery` is performed. In any case, all services and characteristics are discovered. A :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode.FullDiscovery` proceeds and reads all characteristic values and descriptors. A :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode.SkipValueDiscovery` does not read characteristic values and descriptors. A :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode.SkipValueDiscovery` has two advantages. First, it is faster. Second, it circumvents bugs in some devices which wrongly advertise characteristics or descriptors as readable but nevertheless do not permit reads on them. This can trigger unpredictable behavior. After a :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.DiscoveryMode.SkipValueDiscovery`, it is necessary to call :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readCharacteristic` / :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readDescriptor` and wait for them to finish successfully before accessing the value of a characteristic or descriptor.

The argument *mode* was introduced in Qt 6.2.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.state`.
