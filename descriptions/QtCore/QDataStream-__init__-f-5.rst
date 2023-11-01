.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: 6ea7ebd6740c6875ed4b727150d15858

Constructs a read-only data stream that operates on byte array *a*. Use :sip:ref:`~PyQt6.QtCore.QDataStream`\ (\ :sip:ref:`~PyQt6.QtCore.QByteArray`\*, int) if you want to write to a byte array.

Since :sip:ref:`~PyQt6.QtCore.QByteArray` is not a :sip:ref:`~PyQt6.QtCore.QIODevice` subclass, internally a :sip:ref:`~PyQt6.QtCore.QBuffer` is created to wrap the byte array.
