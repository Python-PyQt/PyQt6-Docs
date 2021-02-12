.. sip:method-description::
    :status: todo
    :pysig: 9471a6907986bd629c9d09f90f2c8f04
    :realsig: (const char*,const QVariant&)
    :digest: 953bfc2bf472059a2b987d7b1b38e0b5

Sets the value of the object's *name* property to *value*.

If the property is defined in the class using Q_PROPERTY then true is returned on success and false otherwise. If the property is not defined using Q_PROPERTY, and therefore not listed in the meta-object, it is added as a dynamic property and false is returned.

Information about all available properties is provided through the :sip:ref:`~PyQt6.QtCore.QObject.metaObject` and :sip:ref:`~PyQt6.QtCore.QObject.dynamicPropertyNames`.

Dynamic properties can be queried again using :sip:ref:`~PyQt6.QtCore.QObject.property` and can be removed by setting the property value to an invalid `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_. Changing the value of a dynamic property causes a :sip:ref:`~PyQt6.QtCore.QDynamicPropertyChangeEvent` to be sent to the object.

**Note:** Dynamic properties starting with "_q_" are reserved for internal purposes.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.property`, :sip:ref:`~PyQt6.QtCore.QObject.metaObject`, :sip:ref:`~PyQt6.QtCore.QObject.dynamicPropertyNames`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.write`.
