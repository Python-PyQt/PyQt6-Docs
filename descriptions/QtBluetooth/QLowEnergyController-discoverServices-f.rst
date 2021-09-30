.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: adaf6ab4f34951e87b364cce3f14cd52

Initiates the service discovery process.

The discovery progress is indicated via the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.serviceDiscovered` signal. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.discoveryFinished` signal is emitted when the process has finished.

If the controller instance is not connected or the controller has performed the service discovery already this function will do nothing.

**Note:** Some platforms internally cache the service list of a device which was discovered in the past. This can be problematic if the remote device changed its list of services or their inclusion tree. If this behavior is a problem, the best workaround is to temporarily turn Bluetooth off. This causes a reset of the cache data. Currently Android exhibits such a cache behavior.
