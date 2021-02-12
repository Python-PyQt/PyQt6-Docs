.. sip:class-description::
    :status: todo
    :brief: Meta-data about a property
    :digest: 69f743dc06563f8a88b6bbe0d42d8a87

The :sip:ref:`~PyQt6.QtCore.QMetaProperty` class provides meta-data about a property.

Property meta-data is obtained from an object's meta-object. See :sip:ref:`~PyQt6.QtCore.QMetaObject.property` and :sip:ref:`~PyQt6.QtCore.QMetaObject.propertyCount` for details.

.. _qmetaproperty-property-meta-data:

Property Meta-Data
------------------

A property has a :sip:ref:`~PyQt6.QtCore.QMetaProperty.name` and a type(), as well as various attributes that specify its behavior: :sip:ref:`~PyQt6.QtCore.QMetaProperty.isReadable`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.isWritable`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.isDesignable`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.isScriptable`, revision(), and :sip:ref:`~PyQt6.QtCore.QMetaProperty.isStored`.

If the property is an enumeration, :sip:ref:`~PyQt6.QtCore.QMetaProperty.isEnumType` returns ``true``; if the property is an enumeration that is also a flag (i.e. its values can be combined using the OR operator), :sip:ref:`~PyQt6.QtCore.QMetaProperty.isEnumType` and :sip:ref:`~PyQt6.QtCore.QMetaProperty.isFlagType` both return true. The enumerator for these types is available from :sip:ref:`~PyQt6.QtCore.QMetaProperty.enumerator`.

The property's values are set and retrieved with :sip:ref:`~PyQt6.QtCore.QMetaProperty.read`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.write`, and :sip:ref:`~PyQt6.QtCore.QMetaProperty.reset`; they can also be changed through :sip:ref:`~PyQt6.QtCore.QObject`'s set and get functions. See :sip:ref:`~PyQt6.QtCore.QObject.setProperty` and :sip:ref:`~PyQt6.QtCore.QObject.property` for details.

.. _qmetaproperty-copying-and-assignment:

Copying and Assignment
----------------------

:sip:ref:`~PyQt6.QtCore.QMetaProperty` objects can be copied by value. However, each copy will refer to the same underlying property meta-data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject`, :sip:ref:`~PyQt6.QtCore.QMetaEnum`, :sip:ref:`~PyQt6.QtCore.QMetaMethod`, `Qt's Property System <https://doc.qt.io/qt-6/properties.html>`_.
