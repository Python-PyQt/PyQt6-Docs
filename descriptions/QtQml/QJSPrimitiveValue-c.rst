.. sip:class-description::
    :status: todo
    :brief: Operates on primitive types in JavaScript semantics
    :digest: e16541392ed51bc289b02d7335c2e9fd

The :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue` class operates on primitive types in JavaScript semantics.

:sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue` supports most of the primitive types defined in the `ECMA-262 <https://doc.qt.io/qt-6/http://www.ecma-international.org/publications/standards/Ecma-262.htm>`_ standard, in particular Undefined, Boolean, Number, and String. Additionally, you can store a JavaScript null in a :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue` and as a special case of Number, you can store an integer value.

All those values are stored immediately, without interacting with the JavaScript heap. Therefore, you can pass QJSPrimitiveValues between different JavaScript engines. In contrast to :sip:ref:`~PyQt6.QtQml.QJSManagedValue`, there is also no danger in destroying a :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue` from a different thread than it was created in. On the flip side, :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue` does not hold a reference to any JavaScript engine.

:sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue` implements the JavaScript arithmetic and comparison operators on the supported types in JavaScript semantics. Types are coerced like the JavaScript engine would coerce them if the operators were written in a JavaScript expression.

The JavaScript Symbol type is not supported as it is of very limited utility regarding arithmetic and comparison operators, the main purpose of :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue`. In particular, it causes an exception whenever you try to coerce it to a number or a string, and we cannot throw exceptions without a JavaScript Engine.
