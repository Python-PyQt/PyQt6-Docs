.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: d6c967ebbcc0073c5b7d14f6d5675c1f

An integer. This is a special case of the JavaScript Number type. JavaScript does not have an actual integer type, but the `ECMA-262 <https://doc.qt.io/qt-6/http://www.ecma-international.org/publications/standards/Ecma-262.htm>`_ standard contains rules on how to transform a Number in order to prepare it for certain operators that only make sense on integers, in particular the bit shift operators. :sip:ref:`~PyQt6.QtQml.QJSPrimitiveValue`'s Integer type represents the result of such a transformation.
