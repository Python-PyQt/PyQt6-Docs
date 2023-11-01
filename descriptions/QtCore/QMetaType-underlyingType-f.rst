.. sip:method-description::
    :status: todo
    :pysig: 9f473aba153c000d433dda7b7e46e713
    :realsig: () const
    :digest: 646857b7dc8ca481aeb85b6abd4f3063

If this metatype represents an enumeration, this method returns a metatype of a numeric class of the same signedness and size as the enums underlying type. If it represents a QFlags type, it returns :sip:ref:`~PyQt6.QtCore.QMetaType.Type.Int`. In all other cases an invalid :sip:ref:`~PyQt6.QtCore.QMetaType` is returned.
