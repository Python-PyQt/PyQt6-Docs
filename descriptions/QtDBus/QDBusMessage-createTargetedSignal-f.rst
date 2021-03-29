.. sip:method-description::
    :status: todo
    :pysig: 5009c1d90699a8a77581f6cdb180b294
    :realsig: (const QString&,const QString&,const QString&,const QString&)
    :digest: d325010048abe7c73fda6e9ca11c4c65

Constructs a new DBus message with the given *path*, *interface* and *name*, representing a signal emission to a specific destination.

A DBus signal is emitted from one application and is received only by the application owning the destination *service* name.

The `QDBusMessage <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusmessage>`_ object that is returned can be sent using the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.send` function.
