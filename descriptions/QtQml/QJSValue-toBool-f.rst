.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 260180d4e779d67ab743f800973c8b7c

Returns the boolean value of this :sip:ref:`~PyQt6.QtQml.QJSValue`, using the conversion rules described in `ECMA-262 <https://doc.qt.io/qt-6/http://www.ecma-international.org/publications/standards/Ecma-262.htm>`_ section 9.2, "ToBoolean".

Note that if this :sip:ref:`~PyQt6.QtQml.QJSValue` is an object, calling this function has side effects on the script engine, since the engine will call the object's valueOf() function (and possibly :sip:ref:`~PyQt6.QtQml.QJSValue.toString`) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.isBool`.
