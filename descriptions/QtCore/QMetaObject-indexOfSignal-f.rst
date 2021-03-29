.. sip:method-description::
    :status: todo
    :pysig: 0f9b0ea7a3407ca50e1df7b110b9ad1f
    :realsig: (const char*) const
    :digest: c37c7c868bf04a6e016cb587ce819a2c

Finds *signal* and returns its index; otherwise returns -1.

This is the same as :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfMethod`, except that it will return -1 if the method exists but isn't a signal.

Note that the *signal* has to be in normalized form, as returned by :sip:ref:`~PyQt6.QtCore.QMetaObject.normalizedSignature`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfMethod`, :sip:ref:`~PyQt6.QtCore.QMetaObject.normalizedSignature`, :sip:ref:`~PyQt6.QtCore.QMetaObject.method`, :sip:ref:`~PyQt6.QtCore.QMetaObject.methodCount`, :sip:ref:`~PyQt6.QtCore.QMetaObject.methodOffset`.
