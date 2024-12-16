.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: b54062d9447936e277fdc3fa232fabbf

Returns the alignment of the type in bytes (i.e. alignof(T), where T is the actual type for which this :sip:ref:`~PyQt6.QtCore.QMetaType` instance was constructed for).

This function is typically used together with construct() to perform low-level management of the memory used by a type.

.. seealso:: QMetaType::construct(), :sip:ref:`~PyQt6.QtCore.QMetaType.sizeOf`.
