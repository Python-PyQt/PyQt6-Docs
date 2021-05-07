.. sip:method-description::
    :status: todo
    :pysig: 0749e24123522ed24e2397796579d63f
    :realsig: (const QString&,const QString&,QObject*,QDBusConnection::RegisterOptions)
    :digest: 4a910c03af3f9489b097507879d96b5f

This is an overloaded function.

Registers the object *object* at path *path* with interface name *interface* and returns ``true`` if the registration was successful. The *options* parameter specifies how much of the object *object* will be exposed through D-Bus.

This function does not replace existing objects: if there is already an object registered at path *path*, this function will return false. Use :sip:ref:`~PyQt6.QtDBus.QDBusConnection.unregisterObject` to unregister it first.

The :sip:ref:`~PyQt6.QtDBus.QDBusConnection.RegisterOption.ExportChildObjects` flag exports child objects on D-Bus based on the path of the registered objects and the :sip:ref:`~PyQt6.QtCore.QObject.objectName` of the child. Therefore, it is important for the child object to have an object name.

You cannot register an object as a child object of an object that was registered with :sip:ref:`~PyQt6.QtDBus.QDBusConnection.RegisterOption.ExportChildObjects`.
