.. sip:method-description::
    :status: todo
    :pysig: d57aff5daeae5f6deaa21a4afed71bc9
    :realsig: (quint32, const QJSValue&)
    :digest: 8bc35b41261e34df160eb60189109571

Sets the property at the given *arrayIndex* to the given *value*.

It is possible to modify elements in an array in two ways. The first is to use the array index as the property name:

::

    jsValueArray.setProperty(QLatin1String("4"), value);

The second is to use the overload that takes an index:

::

    jsValueArray.setProperty(4, value);

Both of these approaches achieve the same result, except that the latter:

* Is easier to use (can use an integer directly)

* Is faster (no conversion to integer)

If this :sip:ref:`~PyQt6.QtQml.QJSValue` is not an Array object, this function behaves as if :sip:ref:`~PyQt6.QtQml.QJSValue.setProperty` was called with the string representation of *arrayIndex*.

.. seealso:: property(quint32 arrayIndex), :ref:`qjsvalue-working-with-arrays`.
