.. sip:class-description::
    :status: todo
    :brief: Allows the manipulation of QQmlListProperty properties
    :digest: 6bb159650d0182cd09eaec4c402f8ca3

The :sip:ref:`~PyQt6.QtQml.QQmlListReference` class allows the manipulation of QQmlListProperty properties.

:sip:ref:`~PyQt6.QtQml.QQmlListReference` allows C++ programs to read from, and assign values to a QML list property in a simple and type-safe way. A :sip:ref:`~PyQt6.QtQml.QQmlListReference` can be created by passing an object and property name or through a :sip:ref:`~PyQt6.QtQml.QQmlProperty` instance. These two are equivalent:

::

    QQmlListReference ref1(object, "children");

    QQmlProperty ref2(object, "children");
    QQmlListReference ref2 = qvariant_cast<QQmlListReference>(ref2.read());

Not all QML list properties support all operations. A set of methods, :sip:ref:`~PyQt6.QtQml.QQmlListReference.canAppend`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.canAt`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.canClear` and :sip:ref:`~PyQt6.QtQml.QQmlListReference.canCount` allow programs to query whether an operation is supported on a given property.

QML list properties are type-safe. Only :sip:ref:`~PyQt6.QtCore.QObject`'s that derive from the correct base class can be assigned to the list. The :sip:ref:`~PyQt6.QtQml.QQmlListReference.listElementType` method can be used to query the :sip:ref:`~PyQt6.QtCore.QMetaObject` of the :sip:ref:`~PyQt6.QtCore.QObject` type supported. Attempting to add objects of the incorrect type to a list property will fail.

Like with normal lists, when accessing a list element by index, it is the callers responsibility to ensure that it does not request an out of range element using the :sip:ref:`~PyQt6.QtQml.QQmlListReference.count` method before calling :sip:ref:`~PyQt6.QtQml.QQmlListReference.at`.
