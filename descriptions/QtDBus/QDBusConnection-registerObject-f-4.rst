.. sip:method-description::
    :status: todo
    :pysig: 2b54e1901527bf8e8719d2965bc8f7ea
    :realsig: (const QString&, QObject*, QDBusConnection::RegisterOptions)
    :digest: 655b7974d341d2099b11bda03edfba74

Registers the object *object* at path *path* and returns ``true`` if the registration was successful. The *options* parameter specifies how much of the object *object* will be exposed through D-Bus.

This function does not replace existing objects: if there is already an object registered at path *path*, this function will return false. Use :sip:ref:`~PyQt6.QtDBus.QDBusConnection.unregisterObject` to unregister it first.

The :sip:ref:`~PyQt6.QtDBus.QDBusConnection.RegisterOption.ExportChildObjects` flag exports child objects on D-Bus based on the path of the registered objects and the :sip:ref:`~PyQt6.QtCore.QObject.objectName` of the child. Therefore, it is important for the child object to have an object name.

You cannot register an object as a child object of an object that was registered with :sip:ref:`~PyQt6.QtDBus.QDBusConnection.RegisterOption.ExportChildObjects`.
