.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: cc45fdda3513a82fd217bc42b91a4376

Returns the unsigned 32-bit integer value of this :sip:ref:`~PyQt6.QtQml.QJSValue`, using the conversion rules described in `ECMA-262 <https://doc.qt.io/qt-6/http://www.ecma-international.org/publications/standards/Ecma-262.htm>`_ section 9.6, "ToUint32".

Note that if this :sip:ref:`~PyQt6.QtQml.QJSValue` is an object, calling this function has side effects on the script engine, since the engine will call the object's valueOf() function (and possibly :sip:ref:`~PyQt6.QtQml.QJSValue.toString`) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.toNumber`, :sip:ref:`~PyQt6.QtQml.QJSValue.toInt`.
