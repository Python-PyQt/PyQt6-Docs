.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 3a5c9fbd00ad914b73db830da507875f

Returns the number value of this :sip:ref:`~PyQt6.QtQml.QJSValue`, as defined in `ECMA-262 <https://doc.qt.io/qt-6/http://www.ecma-international.org/publications/standards/Ecma-262.htm>`_ section 9.3, "ToNumber".

Note that if this :sip:ref:`~PyQt6.QtQml.QJSValue` is an object, calling this function has side effects on the script engine, since the engine will call the object's valueOf() function (and possibly :sip:ref:`~PyQt6.QtQml.QJSValue.toString`) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.isNumber`, :sip:ref:`~PyQt6.QtQml.QJSValue.toInt`, :sip:ref:`~PyQt6.QtQml.QJSValue.toUInt`.
