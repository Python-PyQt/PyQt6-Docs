.. sip:method-description::
    :status: todo
    :pysig: 7cc0a9a6b379955470bc55a82df94e85
    :realsig: (const QString&, QDBusConnection::UnregisterMode)
    :digest: 3a8825a8c4f34331cc1db678c0ed2b36

Unregisters an object that was registered with the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.registerObject` at the object path given by *path* and, if *mode* is :sip:ref:`~PyQt6.QtDBus.QDBusConnection.UnregisterMode.UnregisterTree`, all of its sub-objects too.

Note that you cannot unregister objects that were not registered with :sip:ref:`~PyQt6.QtDBus.QDBusConnection.registerObject`.
