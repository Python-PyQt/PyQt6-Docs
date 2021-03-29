.. sip:method-description::
    :status: todo
    :pysig: 464815642174e41784170637af7f5ee8
    :realsig: (const QDBusConnection&)
    :digest: 9bed7d57d8bbe69c04ad020d8656ab1d

Sets the D-Bus connection that this object is attached to be *connection*. All services watched will be transferred to this connection.

Note that `QDBusConnection <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusconnection>`_ objects are reference counted: :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher` will keep a reference for this connection while it exists. The connection is not closed until the reference count drops to zero, so this will ensure that any notifications are received while this :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher` object exists.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.connection`.
