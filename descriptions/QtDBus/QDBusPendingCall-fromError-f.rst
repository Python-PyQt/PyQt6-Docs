.. sip:method-description::
    :status: todo
    :pysig: f52b5ec10ba89ad59d1dcd4334331129
    :realsig: (const QDBusError&)
    :digest: 99ea0d741d4feea0da074a3eac83321b

Creates a :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall` object based on the error condition *error*. The resulting pending call object will be in the "finished" state and `QDBusPendingReply <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbuspendingreply>`_<Types...>::isError() will return true.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall.fromCompletedCall`.
