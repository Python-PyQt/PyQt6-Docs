.. sip:method-description::
    :status: todo
    :pysig: c70916e782d9742b90f37ccdedc4f900
    :realsig: (const QByteArray&)
    :digest: 6ea7ebd6740c6875ed4b727150d15858

Constructs a read-only data stream that operates on byte array *a*. Use :sip:ref:`~PyQt6.QtCore.QDataStream`\ (\ :sip:ref:`~PyQt6.QtCore.QByteArray`\*, int) if you want to write to a byte array.

Since :sip:ref:`~PyQt6.QtCore.QByteArray` is not a :sip:ref:`~PyQt6.QtCore.QIODevice` subclass, internally a :sip:ref:`~PyQt6.QtCore.QBuffer` is created to wrap the byte array.
