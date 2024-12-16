.. sip:method-description::
    :status: todo
    :pysig: d084f1c21b1a1d68ff5094948afc4fc3
    :realsig: (const QString&) const
    :digest: 695099e2d7da3dbf52ce443e78fd6dd0

Returns the value of this :sip:ref:`~PyQt6.QtQml.QJSValue`'s property with the given *name*. If no such property exists, an undefined :sip:ref:`~PyQt6.QtQml.QJSValue` is returned.

If the property is implemented using a getter function (i.e. has the PropertyGetter flag set), calling property() has side-effects on the script engine, since the getter function will be called (possibly resulting in an uncaught script exception). If an exception occurred, property() returns the value that was thrown (typically an ``Error`` object).

To access array elements, use the setProperty(quint32 arrayIndex, const QJSValue &value) overload instead.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.setProperty`, :sip:ref:`~PyQt6.QtQml.QJSValue.hasProperty`, :sip:ref:`~PyQt6.QtQml.QJSValueIterator`.
