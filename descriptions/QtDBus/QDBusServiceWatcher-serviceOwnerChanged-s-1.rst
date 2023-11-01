.. sip:signal-description::
    :status: todo
    :pysig: 31c2d3982cfaf905cac8e2c6560b0db1
    :realsig: (const QString&, const QString&, const QString&)
    :digest: 7ee5b68568a4034124c548e4cb6f135b

This signal is emitted whenever this object detects that there was a service ownership change relating to the *serviceName* service. The *oldOwner* parameter contains the old owner name and *newOwner* is the new owner. Both *oldOwner* and *newOwner* are unique connection names.

Note that this signal is also emitted whenever the *serviceName* service was registered or unregistered. If it was registered, *oldOwner* will contain an empty string, whereas if it was unregistered, *newOwner* will contain an empty string.

If you need only to find out if the service is registered or unregistered only, without being notified that the ownership changed, consider using the specific modes for those operations. This class is more efficient if you use the more specific modes.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.serviceRegistered`, :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.serviceUnregistered`.
