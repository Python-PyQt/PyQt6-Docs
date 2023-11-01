.. sip:method-description::
    :status: todo
    :pysig: 560db1b82ea71534364422b0ed235b37
    :realsig: (const QString&, const QString&, const QString&, const QDBusConnection&, QObject*)
    :digest: 614aef4c9fae833046a90dcbb5465588

Creates a dynamic :sip:ref:`~PyQt6.QtDBus.QDBusInterface` object associated with the interface *interface* on object at path *path* on service *service*, using the given *connection*. If *interface* is an empty string, the object created will refer to the merging of all interfaces found by introspecting that object. Otherwise if *interface* is not empty, the :sip:ref:`~PyQt6.QtDBus.QDBusInterface` object will be cached to speedup further creations of the same interface.

*parent* is passed to the base class constructor.

If the remote service *service* is not present or if an error occurs trying to obtain the description of the remote interface *interface*, the object created will not be valid (see isValid()).
