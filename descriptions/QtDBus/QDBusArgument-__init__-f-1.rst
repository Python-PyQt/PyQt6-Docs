.. sip:method-description::
    :status: todo
    :pysig: 03a575f23c095de6e2fd49e946cb5c43
    :realsig: (const QDBusArgument&)
    :digest: 751214f8d8d4d34f63b1bd3c0987e495

Constructs a copy of the *other* `QDBusArgument <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusargument>`_ object.

Both objects will therefore contain the same state from this point forward. QDBusArguments are explicitly shared and, therefore, any modification to either copy will affect the other one too.
