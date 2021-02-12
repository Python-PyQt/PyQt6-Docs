.. sip:method-description::
    :status: todo
    :pysig: 9d07db3855925cb51c73b4c90bff627d
    :realsig: (QByteArray*,QIODeviceBase::OpenMode)
    :digest: 90a4b5a9388b97195cddf7a347676ab5

Constructs a data stream that operates on a byte array, *a*. The *mode* describes how the device is to be used.

Alternatively, you can use :sip:ref:`~PyQt6.QtCore.QDataStream`\ (const :sip:ref:`~PyQt6.QtCore.QByteArray` &) if you just want to read from a byte array.

Since :sip:ref:`~PyQt6.QtCore.QByteArray` is not a :sip:ref:`~PyQt6.QtCore.QIODevice` subclass, internally a :sip:ref:`~PyQt6.QtCore.QBuffer` is created to wrap the byte array.
