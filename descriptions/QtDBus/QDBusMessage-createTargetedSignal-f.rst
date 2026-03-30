.. sip:method-description::
    :status: todo
    :pysig: 915a0ceffabdcf7d6d34040ff9eabf37
    :realsig: (const QString&, const QString&, const QString&, const QString&)
    :digest: d325010048abe7c73fda6e9ca11c4c65

Constructs a new DBus message with the given *path*, *interface* and *name*, representing a signal emission to a specific destination.

A DBus signal is emitted from one application and is received only by the application owning the destination *service* name.

The :sip:ref:`~PyQt6.QtDBus.QDBusMessage` object that is returned can be sent using the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.send` function.
