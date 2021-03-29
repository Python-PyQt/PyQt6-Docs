.. sip:class-description::
    :status: todo
    :brief: Represents an error received from the D-Bus bus or from remote applications found in the bus
    :digest: 9fb88cca56c548e409064112efdbcf2d

The :sip:ref:`~PyQt6.QtDBus.QDBusError` class represents an error received from the D-Bus bus or from remote applications found in the bus.

When dealing with the D-Bus bus service or with remote applications over D-Bus, a number of error conditions can happen. This error conditions are sometimes signalled by a returned error value or by a :sip:ref:`~PyQt6.QtDBus.QDBusError`.

C++ and Java exceptions are a valid analogy for D-Bus errors: instead of returning normally with a return value, remote applications and the bus may decide to throw an error condition. However, the Qt D-Bus implementation does not use the C++ exception-throwing mechanism, so you will receive QDBusErrors in the return reply (see QDBusReply::error()).

:sip:ref:`~PyQt6.QtDBus.QDBusError` objects are used to inspect the error name and message as received from the bus and remote applications. You should not create such objects yourself to signal error conditions when called from D-Bus: instead, use :sip:ref:`~PyQt6.QtDBus.QDBusMessage.createError` and :sip:ref:`~PyQt6.QtDBus.QDBusConnection.send`.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusConnection.send`, `QDBusMessage <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusmessage>`_, QDBusReply.
