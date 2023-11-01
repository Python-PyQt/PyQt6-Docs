.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 20f6cb68a18cd31e03203f086e27ae5b

Removes the *service* from the list of services being watched by this object. Note that D-Bus notifications are asynchronous, so there may still be signals pending delivery about *service*. Those signals will still be emitted whenever the D-Bus messages are processed.

Removes any existing binding of :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.watchedServices`.

This function returns ``true`` if any services were removed.
