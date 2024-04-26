.. sip:method-description::
    :status: todo
    :pysig: 9f473aba153c000d433dda7b7e46e713
    :realsig: () const
    :digest: 944374304a65716a87537e3d0e0ba439

Returns the meta type of the enum.

If the :sip:ref:`~PyQt6.QtCore.QMetaObject` that this enum is part of was generated with Qt 6.5 or earlier, this will be an invalid meta type.

**Note:** This is the meta type of the enum itself, not of its underlying integral type. You can retrieve the meta type of the underlying type of the enum using :sip:ref:`~PyQt6.QtCore.QMetaType.underlyingType`.
