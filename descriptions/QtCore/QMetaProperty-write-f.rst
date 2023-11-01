.. sip:method-description::
    :status: todo
    :pysig: 2a5da58ea00aada7c7bf751dae85c723
    :realsig: (QObject*,const QVariant&) const
    :digest: a7cce0442632c115befc6d2c82109a91

Writes *value* as the property's value to the given *object*. Returns true if the write succeeded; otherwise returns ``false``.

If *value* is not of the same type as the property, a conversion is attempted. An empty QVariant() is equivalent to a call to :sip:ref:`~PyQt6.QtCore.QMetaProperty.reset` if this property is resettable, or setting a default-constructed object otherwise.

**Note:** This function internally makes a copy of *value*. Prefer to use the rvalue overload when possible.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaProperty.read`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.reset`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.isWritable`.
