.. sip:method-description::
    :status: todo
    :pysig: e78af8dd7b58e8332d7100878c7a7116
    :realsig: (const QString&, const QJSValue&)
    :digest: 1b0e37450493c1a62c398f090d55f784

Sets the value of this :sip:ref:`~PyQt6.QtQml.QJSValue`'s property with the given *name* to the given *value*.

If this :sip:ref:`~PyQt6.QtQml.QJSValue` is not an object, this function does nothing.

If this :sip:ref:`~PyQt6.QtQml.QJSValue` does not already have a property with name *name*, a new property is created.

To modify array elements, use the setProperty(quint32 arrayIndex, const QJSValue &value) overload instead.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.property`, :sip:ref:`~PyQt6.QtQml.QJSValue.deleteProperty`.
