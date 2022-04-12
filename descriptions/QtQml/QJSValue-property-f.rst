.. sip:method-description::
    :status: todo
    :pysig: ee4163cc141154e5c0774a9f9c667938
    :realsig: (const QString&) const
    :digest: e8e308969248500bab63736668b5467a

Returns the value of this :sip:ref:`~PyQt6.QtQml.QJSValue`'s property with the given *name*. If no such property exists, an undefined :sip:ref:`~PyQt6.QtQml.QJSValue` is returned.

If the property is implemented using a getter function (i.e. has the PropertyGetter flag set), calling  has side-effects on the script engine, since the getter function will be called (possibly resulting in an uncaught script exception). If an exception occurred,  returns the value that was thrown (typically an ``Error`` object).

To access array elements, use the setProperty(quint32 arrayIndex, const QJSValue &value) overload instead.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.setProperty`, :sip:ref:`~PyQt6.QtQml.QJSValue.hasProperty`, :sip:ref:`~PyQt6.QtQml.QJSValueIterator`.
