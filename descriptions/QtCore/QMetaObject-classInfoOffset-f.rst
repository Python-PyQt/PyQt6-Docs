.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: a2cf8e583ebb94e00aa950a49eedf191

Returns the class information offset for this class; i.e. the index position of this class's first class information item.

If the class has no superclasses with class information, the offset is 0; otherwise the offset is the sum of all the class information items in the class's superclasses.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.classInfo`, :sip:ref:`~PyQt6.QtCore.QMetaObject.classInfoCount`, :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfClassInfo`.
