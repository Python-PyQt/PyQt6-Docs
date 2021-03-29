.. sip:method-description::
    :status: todo
    :pysig: b1e28526f6f973396094ec9441a8c59e
    :realsig: (const QString&,const QString&,const QString&)
    :digest: 0543ecc0f8894780275fb1d35be739d3

Constructs a new DBus message with the given *path*, *interface* and *name*, representing a signal emission.

A DBus signal is emitted from one application and is received by all applications that are listening for that signal from that interface.

The `QDBusMessage <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusmessage>`_ object that is returned can be sent using the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.send` function.
