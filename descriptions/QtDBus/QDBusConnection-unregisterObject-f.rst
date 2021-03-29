.. sip:method-description::
    :status: todo
    :pysig: c0c87b72bf26ba7c0aceec0637b6c83c
    :realsig: (const QString&,QDBusConnection::UnregisterMode)
    :digest: 3a8825a8c4f34331cc1db678c0ed2b36

Unregisters an object that was registered with the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.registerObject` at the object path given by *path* and, if *mode* is :sip:ref:`~PyQt6.QtDBus.QDBusConnection.UnregisterMode.UnregisterTree`, all of its sub-objects too.

Note that you cannot unregister objects that were not registered with :sip:ref:`~PyQt6.QtDBus.QDBusConnection.registerObject`.
