.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 64340d627b72cde432b64126850830a9

Returns the string value of this :sip:ref:`~PyQt6.QtQml.QJSValue`, as defined in `ECMA-262 <https://doc.qt.io/qt-6/http://www.ecma-international.org/publications/standards/Ecma-262.htm>`_ section 9.8, "ToString".

Note that if this :sip:ref:`~PyQt6.QtQml.QJSValue` is an object, calling this function has side effects on the script engine, since the engine will call the object's  function (and possibly valueOf()) in an attempt to convert the object to a primitive value (possibly resulting in an uncaught script exception).

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.isString`.
