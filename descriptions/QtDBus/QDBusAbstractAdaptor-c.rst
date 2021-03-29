.. sip:class-description::
    :status: todo
    :brief: The base class of D-Bus adaptor classes
    :digest: 87860840064bfd742580faf29c30c0ae

The :sip:ref:`~PyQt6.QtDBus.QDBusAbstractAdaptor` class is the base class of D-Bus adaptor classes.

The :sip:ref:`~PyQt6.QtDBus.QDBusAbstractAdaptor` class is the starting point for all objects intending to provide interfaces to the external world using D-Bus. This is accomplished by attaching a one or more classes derived from :sip:ref:`~PyQt6.QtDBus.QDBusAbstractAdaptor` to a normal :sip:ref:`~PyQt6.QtCore.QObject` and then registering that :sip:ref:`~PyQt6.QtCore.QObject` with :sip:ref:`~PyQt6.QtDBus.QDBusConnection.registerObject`. :sip:ref:`~PyQt6.QtDBus.QDBusAbstractAdaptor` objects are intended to be light-weight wrappers, mostly just relaying calls into the real object (its parent) and the signals from it.

Each :sip:ref:`~PyQt6.QtDBus.QDBusAbstractAdaptor`-derived class should define the D-Bus interface it is implementing using the Q_CLASSINFO macro in the class definition. Note that only one interface can be exposed in this way.

:sip:ref:`~PyQt6.QtDBus.QDBusAbstractAdaptor` uses the standard :sip:ref:`~PyQt6.QtCore.QObject` mechanism of signals, slots and properties to determine what signals, methods and properties to export to the bus. Any signal emitted by :sip:ref:`~PyQt6.QtDBus.QDBusAbstractAdaptor`-derived classes will be automatically be relayed through any D-Bus connections the object is registered on.

Classes derived from :sip:ref:`~PyQt6.QtDBus.QDBusAbstractAdaptor` must be created on the heap using the *new* operator and must not be deleted by the user (they will be deleted automatically when the object they are connected to is also deleted).

.. seealso:: `Using adaptors <https://doc.qt.io/qt-6/usingadaptors.html>`_, `QDBusConnection <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusconnection>`_.
