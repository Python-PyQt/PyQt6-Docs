.. sip:method-description::
    :status: todo
    :pysig: 24debb920ae037a67e401e6ba5c08526
    :realsig: (const QJSValue&) const
    :digest: 1f3f636a57d92fd991e529793437d5f7

Returns true if this :sip:ref:`~PyQt6.QtQml.QJSValue` is equal to *other*, otherwise returns false. The comparison follows the behavior described in `ECMA-262 <https://doc.qt.io/qt-6/http://www.ecma-international.org/publications/standards/Ecma-262.htm>`_ section 11.9.3, "The Abstract Equality Comparison Algorithm".

This function can return true even if the type of this :sip:ref:`~PyQt6.QtQml.QJSValue` is different from the type of the *other* value; i.e. the comparison is not strict. For example, comparing the number 9 to the string "9" returns true; comparing an undefined value to a null value returns true; comparing a ``Number`` object whose primitive value is 6 to a ``String`` object whose primitive value is "6" returns true; and comparing the number 1 to the boolean value ``true`` returns true. If you want to perform a comparison without such implicit value conversion, use :sip:ref:`~PyQt6.QtQml.QJSValue.strictlyEquals`.

Note that if this :sip:ref:`~PyQt6.QtQml.QJSValue` or the *other* value are objects, calling this function has side effects on the script engine, since the engine will call the object's valueOf() function (and possibly :sip:ref:`~PyQt6.QtQml.QJSValue.toString`) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.strictlyEquals`.
