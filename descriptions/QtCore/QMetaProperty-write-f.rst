.. sip:method-description::
    :status: todo
    :pysig: 2a5da58ea00aada7c7bf751dae85c723
    :realsig: (QObject*,const QVariant&) const
    :digest: da1c7624a3f8f90520dddb791badf667

Writes *value* as the property's value to the given *object*. Returns true if the write succeeded; otherwise returns ``false``.

If *value* is not of the same type type as the property, a conversion is attempted. An empty `QVariant() <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ is equivalent to a call to :sip:ref:`~PyQt6.QtCore.QMetaProperty.reset` if this property is resetable, or setting a default-constructed object otherwise.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaProperty.read`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.reset`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.isWritable`.
