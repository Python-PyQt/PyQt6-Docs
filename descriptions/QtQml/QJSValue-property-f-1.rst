.. sip:method-description::
    :status: todo
    :pysig: 5c4e70403d70c0ed1ef1ab5908fdbb14
    :realsig: (quint32) const
    :digest: 57979ff767c3a96bf016fdd8c0ad0628

This is an overloaded function.

Returns the property at the given *arrayIndex*.

It is possible to access elements in an array in two ways. The first is to use the array index as the property name:

::

    qDebug() << jsValueArray.property(QLatin1String("4")).toString();

The second is to use the overload that takes an index:

::

    qDebug() << jsValueArray.property(4).toString();

Both of these approaches achieve the same result, except that the latter:

* Is easier to use (can use an integer directly)

* Is faster (no conversion to integer)

If this :sip:ref:`~PyQt6.QtQml.QJSValue` is not an Array object, this function behaves as if :sip:ref:`~PyQt6.QtQml.QJSValue.property` was called with the string representation of *arrayIndex*.
