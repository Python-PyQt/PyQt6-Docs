.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&)
    :digest: aba604d9e980ff787e36c246f8f5f42c

Attempts to delete this object's property of the given *name*. Returns true if the property was deleted, otherwise returns false.

The behavior of this function is consistent with the JavaScript delete operator. In particular:

* Non-configurable properties cannot be deleted.

* This function will return true even if this object doesn't have a property of the given *name* (i.e., non-existent properties are "trivially deletable").

* If this object doesn't have an own property of the given *name*, but an object in the :sip:ref:`~PyQt6.QtQml.QJSValue.prototype` chain does, the prototype object's property is not deleted, and this function returns true.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.setProperty`, :sip:ref:`~PyQt6.QtQml.QJSValue.hasOwnProperty`.
