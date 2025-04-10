.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: c3616324ac049b18e1a690c1569c4f57

Returns the return type name of this method. If this method is a constructor, this function returns an empty string (constructors have no return types).

**Note:** In Qt 7, this function will return a null pointer for constructors.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaMethod.returnType`, QMetaType::type().
