.. sip:method-description::
    :status: todo
    :pysig: 0f9b0ea7a3407ca50e1df7b110b9ad1f
    :realsig: (const char*) const
    :digest: 6b5f8c4845b2923e1ddc3a28ac2523e2

Finds *slot* and returns its index; otherwise returns -1.

This is the same as :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfMethod`, except that it will return -1 if the method exists but isn't a slot.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfMethod`, :sip:ref:`~PyQt6.QtCore.QMetaObject.method`, :sip:ref:`~PyQt6.QtCore.QMetaObject.methodCount`, :sip:ref:`~PyQt6.QtCore.QMetaObject.methodOffset`.
