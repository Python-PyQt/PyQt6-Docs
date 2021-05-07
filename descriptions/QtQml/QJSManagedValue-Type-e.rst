.. sip:enum-description::
    :status: todo
    :digest: 8cd2455c4edca1fb3d555124827cc76b

This enum represents the JavaScript native types, as specified by `ECMA-262 <https://doc.qt.io/qt-6/http://www.ecma-international.org/publications/standards/Ecma-262.htm>`_.

Note that the ``null`` value is not a type of itself but rather a special kind of object. You can query a :sip:ref:`~PyQt6.QtQml.QJSManagedValue` for this condition using the :sip:ref:`~PyQt6.QtQml.QJSManagedValue.isNull` method. Furthermore, JavaScript has no integer type, but it knows a special treatment of numbers in preparation for integer only operations. You can query a :sip:ref:`~PyQt6.QtQml.QJSManagedValue` to find out whether it holds the result of such a treatment by using the :sip:ref:`~PyQt6.QtQml.QJSManagedValue.isInteger` method.
