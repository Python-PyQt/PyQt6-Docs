.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 7b54308818fa3888cf3c83c20e7d7664

Adds *newService* to the list of services to be watched by this object. This function is more efficient than :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.setWatchedServices` and should be used whenever possible to add services.

Removes any existing binding of :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.watchedServices`.
