.. sip:class-description::
    :status: todo
    :brief: Acts as a container for Qt/JavaScript data types
    :digest: 306023fbbfdbecce278595140659f579

The :sip:ref:`~PyQt6.QtQml.QJSValue` class acts as a container for Qt/JavaScript data types.

:sip:ref:`~PyQt6.QtQml.QJSValue` supports the types defined in the `ECMA-262 <https://doc.qt.io/qt-6/https://www.ecma-international.org/publications-and-standards/standards/ecma-262/>`_ standard: The primitive types, which are Undefined, Null, Boolean, Number, and String; and the Object and Array types. Additionally, built-in support is provided for Qt/C++ types such as :sip:ref:`~PyQt6.QtCore.QVariant` and :sip:ref:`~PyQt6.QtCore.QObject`.

For the object-based types (including Date and RegExp), use the newT() functions in :sip:ref:`~PyQt6.QtQml.QJSEngine` (e.g. :sip:ref:`~PyQt6.QtQml.QJSEngine.newObject`) to create a :sip:ref:`~PyQt6.QtQml.QJSValue` of the desired type. For the primitive types, use one of the :sip:ref:`~PyQt6.QtQml.QJSValue` constructor overloads. For other types, e.g. registered gadget types such as :sip:ref:`~PyQt6.QtCore.QPoint`, you can use :sip:ref:`~PyQt6.QtQml.QJSEngine.toScriptValue`.

The methods named isT() (e.g. :sip:ref:`~PyQt6.QtQml.QJSValue.isBool`, :sip:ref:`~PyQt6.QtQml.QJSValue.isUndefined`) can be used to test if a value is of a certain type. The methods named toT() (e.g. :sip:ref:`~PyQt6.QtQml.QJSValue.toBool`, :sip:ref:`~PyQt6.QtQml.QJSValue.toString`) can be used to convert a :sip:ref:`~PyQt6.QtQml.QJSValue` to another type. You can also use the generic qjsvalue_cast() function.

Object values have zero or more properties which are themselves QJSValues. Use :sip:ref:`~PyQt6.QtQml.QJSValue.setProperty` to set a property of an object, and call :sip:ref:`~PyQt6.QtQml.QJSValue.property` to retrieve the value of a property.

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_script_qjsvalue.py
    :lines: 54-58

If you want to iterate over the properties of a script object, use the :sip:ref:`~PyQt6.QtQml.QJSValueIterator` class.

Object values have an internal ``prototype`` property, which can be accessed with :sip:ref:`~PyQt6.QtQml.QJSValue.prototype` and :sip:ref:`~PyQt6.QtQml.QJSValue.setPrototype`.

Function objects (objects for which :sip:ref:`~PyQt6.QtQml.QJSValue.isCallable`) returns true) can be invoked by calling :sip:ref:`~PyQt6.QtQml.QJSValue.call`. Constructor functions can be used to construct new objects by calling :sip:ref:`~PyQt6.QtQml.QJSValue.callAsConstructor`.

Use :sip:ref:`~PyQt6.QtQml.QJSValue.equals` or :sip:ref:`~PyQt6.QtQml.QJSValue.strictlyEquals` to compare a :sip:ref:`~PyQt6.QtQml.QJSValue` to another.

Note that a :sip:ref:`~PyQt6.QtQml.QJSValue` for which :sip:ref:`~PyQt6.QtQml.QJSValue.isObject` is true only carries a reference to an actual object; copying the :sip:ref:`~PyQt6.QtQml.QJSValue` will only copy the object reference, not the object itself. If you want to clone an object (i.e. copy an object's properties to another object), you can do so with the help of a ``for-in`` statement in script code, or :sip:ref:`~PyQt6.QtQml.QJSValueIterator` in C++.

.. _qjsvalue-working-with-arrays:

Working With Arrays
-------------------

To create an array using :sip:ref:`~PyQt6.QtQml.QJSValue`, use :sip:ref:`~PyQt6.QtQml.QJSEngine.newArray`:

::

    // Assumes that this class was declared in QML.
    QJSValue jsArray = engine->newArray(3);

To set individual elements in the array, use the setProperty(quint32 arrayIndex, const QJSValue &value) overload. For example, to fill the array above with integers:

::

    for (int i = 0; i < 3; ++i) {
        jsArray.setProperty(i, QRandomGenerator::global().generate());
    }

To determine the length of the array, access the ``"length"`` property. To access array elements, use the property(quint32 arrayIndex) overload. The following code reads the array we created above back into a list:

::

    QVector<int> integers;
    const int length = jsArray.property("length").toInt();
    for (int i = 0; i < length; ++i) {
        integers.append(jsArray.property(i).toInt());
    }

.. _qjsvalue-converting-to-json:

Converting to JSON
..................

It's possible to convert a :sip:ref:`~PyQt6.QtQml.QJSValue` to a JSON type. For example, to convert to an array, use QJSEngine::fromScriptValue():

::

    const QJsonValue jsonValue = engine.fromScriptValue<QJsonValue>(jsValue);
    const QJsonArray jsonArray = jsonValue.toArray();

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSEngine`, :sip:ref:`~PyQt6.QtQml.QJSValueIterator`.
