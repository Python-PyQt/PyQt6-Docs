.. sip:method-description::
    :status: todo
    :pysig: 5009c1d90699a8a77581f6cdb180b294
    :realsig: (const QString&,const QString&,const QString&,const QString&)
    :digest: 26374122cc7690df7a72965a8c6fd093

Constructs a new DBus message representing a method call. A method call always informs its destination address (\ *service*, *path*, *interface* and *method*).

The DBus bus allows calling a method on a given remote object without specifying the destination interface, if the method name is unique. However, if two interfaces on the remote object export the same method name, the result is undefined (one of the two may be called or an error may be returned).

When using DBus in a peer-to-peer context (i.e., not on a bus), the *service* parameter is optional.

The :sip:ref:`~PyQt6.QtDBus.QDBusInterface` class provides a simpler abstraction to synchronous method calling.

This function returns a `QDBusMessage <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusmessage>`_ object that can be sent with :sip:ref:`~PyQt6.QtDBus.QDBusConnection.call`.
