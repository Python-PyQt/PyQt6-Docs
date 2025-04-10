.. sip:class-description::
    :status: todo
    :brief: Allows the manipulation of QQmlListProperty properties
    :digest: 580e8533d2e0bae049e17b20fd155c5d

The :sip:ref:`~PyQt6.QtQml.QQmlListReference` class allows the manipulation of QQmlListProperty properties.

:sip:ref:`~PyQt6.QtQml.QQmlListReference` allows C++ programs to read from, and assign values to a QML list property in a simple and type-safe way. The main advantage over using QQmlListProperty itself is its type erasure: :sip:ref:`~PyQt6.QtQml.QQmlListReference` is not a template, but can be used for QQmlListProperties of any type. Furthermore it watches the owner object for deletion and does not allow the QQmlListProperty to be accessed anymore if its owner has been deleted.

You can create a :sip:ref:`~PyQt6.QtQml.QQmlListReference` from either an object and a property name or from a :sip:ref:`~PyQt6.QtCore.QVariant`. These two are equivalent:

::

    QQmlListReference ref1(object, "children");

    const QVariant var = object->property("children");
    QQmlListReference ref2(var);

Not all QQmlListReferences support all operations. Methods like :sip:ref:`~PyQt6.QtQml.QQmlListReference.canAppend`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.canAt`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.canClear`, and :sip:ref:`~PyQt6.QtQml.QQmlListReference.canCount` allow programs to query whether an operation is supported on a given property. The availability of the methods depends on the methods implemented by the underlying QQmlListProperty. When constructing a QQmlListProperty by manually passing the accessor functions you can restrict access to the list by passing nullptr to some of them. :sip:ref:`~PyQt6.QtQml.QQmlListReference` will recognize those and report them as unavailable.

:sip:ref:`~PyQt6.QtQml.QQmlListReference`\ s are type-safe. Only :sip:ref:`~PyQt6.QtCore.QObject`\ s that derive of the correct base class can be added to the list. The :sip:ref:`~PyQt6.QtQml.QQmlListReference.listElementType` method can be used to query the :sip:ref:`~PyQt6.QtCore.QMetaObject` of the :sip:ref:`~PyQt6.QtCore.QObject` type that can be added. Attempting to add objects of an incorrect type to a list property will fail.

Like with other lists, when accessing a list element by index, it is the callers responsibility to ensure that it does not request an out of range element. Use the :sip:ref:`~PyQt6.QtQml.QQmlListReference.count` method before calling :sip:ref:`~PyQt6.QtQml.QQmlListReference.at` to this effect.
