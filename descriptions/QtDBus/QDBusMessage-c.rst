.. sip:class-description::
    :status: todo
    :brief: Represents one message sent or received over the D-Bus bus
    :digest: aa4b45dbb823681f4fb15974d3ed569d

The `QDBusMessage <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusmessage>`_ class represents one message sent or received over the D-Bus bus.

This object can represent any of the four different types of messages (\ :sip:ref:`~PyQt6.QtDBus.QDBusMessage.MessageType.MessageType`) that can occur on the bus:

* Method calls

* Method return values

* Signal emissions

* Error codes

Objects of this type are created with the static :sip:ref:`~PyQt6.QtDBus.QDBusMessage.createError`, :sip:ref:`~PyQt6.QtDBus.QDBusMessage.createMethodCall` and :sip:ref:`~PyQt6.QtDBus.QDBusMessage.createSignal` functions. Use the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.send` function to send the messages.
