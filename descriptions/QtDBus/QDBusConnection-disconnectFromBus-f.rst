.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: (const QString&)
    :digest: 08b2fecf3903b806f483e16e72bc8a77

Closes the bus connection of name *name*.

Note that if there are still `QDBusConnection <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusconnection>`_ objects associated with the same connection, the connection will not be closed until all references are dropped. However, no further references can be created using the `QDBusConnection <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusconnection>`_ constructor.
