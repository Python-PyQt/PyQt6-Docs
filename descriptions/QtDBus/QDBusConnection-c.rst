.. sip:class-description::
    :status: todo
    :brief: Represents a connection to the D-Bus bus daemon
    :digest: 911887ea722b4fa83db1e93f827eeff1

The `QDBusConnection <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusconnection>`_ class represents a connection to the D-Bus bus daemon.

This class is the initial point in a D-Bus session. Using it, you can get access to remote objects, interfaces; connect remote signals to your object's slots; register objects, etc.

D-Bus connections are created using the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.connectToBus` function, which opens a connection to the server daemon and does the initial handshaking, associating that connection with a name. Further attempts to connect using the same name will return the same connection.

The connection is then torn down using the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.disconnectFromBus` function.

Once disconnected, calling :sip:ref:`~PyQt6.QtDBus.QDBusConnection.connectToBus` will not reestablish a connection, you must create a new `QDBusConnection <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusconnection>`_ instance.

As a convenience for the two most common connection types, the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.sessionBus` and :sip:ref:`~PyQt6.QtDBus.QDBusConnection.systemBus` functions return open connections to the session server daemon and the system server daemon, respectively. Those connections are opened when first used and are closed when the :sip:ref:`~PyQt6.QtCore.QCoreApplication` destructor is run.

D-Bus also supports peer-to-peer connections, without the need for a bus server daemon. Using this facility, two applications can talk to each other and exchange messages. This can be achieved by passing an address to :sip:ref:`~PyQt6.QtDBus.QDBusConnection.connectToBus` function, which was opened by another D-Bus application using QDBusServer.
