.. sip:method-description::
    :status: todo
    :pysig: 43712e4740fe2d94b75f1e5f66615ef8
    :realsig: (QByteArray*,QIODeviceBase::OpenMode)
    :digest: 90a4b5a9388b97195cddf7a347676ab5

Constructs a data stream that operates on a byte array, *a*. The *mode* describes how the device is to be used.

Alternatively, you can use :sip:ref:`~PyQt6.QtCore.QDataStream`\ (const :sip:ref:`~PyQt6.QtCore.QByteArray` &) if you just want to read from a byte array.

Since :sip:ref:`~PyQt6.QtCore.QByteArray` is not a :sip:ref:`~PyQt6.QtCore.QIODevice` subclass, internally a :sip:ref:`~PyQt6.QtCore.QBuffer` is created to wrap the byte array.
