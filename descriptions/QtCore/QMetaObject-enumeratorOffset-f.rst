.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: ff977406c97b1911ae3e1c095d351789

Returns the enumerator offset for this class; i.e. the index position of this class's first enumerator.

If the class has no superclasses with enumerators, the offset is 0; otherwise the offset is the sum of all the enumerators in the class's superclasses.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.enumerator`, :sip:ref:`~PyQt6.QtCore.QMetaObject.enumeratorCount`, :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfEnumerator`.
