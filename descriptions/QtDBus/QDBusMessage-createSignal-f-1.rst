.. sip:method-description::
    :status: todo
    :pysig: 750a42330c864fea6553fa00506ff1d4
    :realsig: (const QString&, const QString&, const QString&)
    :digest: 0543ecc0f8894780275fb1d35be739d3

Constructs a new DBus message with the given *path*, *interface* and *name*, representing a signal emission.

A DBus signal is emitted from one application and is received by all applications that are listening for that signal from that interface.

The :sip:ref:`~PyQt6.QtDBus.QDBusMessage` object that is returned can be sent using the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.send` function.
