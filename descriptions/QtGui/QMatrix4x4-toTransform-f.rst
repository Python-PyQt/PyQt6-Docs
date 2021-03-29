.. sip:method-description::
    :status: todo
    :pysig: e27247e5b452ce98dcfc93f19679f890
    :realsig: () const
    :digest: a723aece066f8bf3ed8be94bb20c23b3

Returns the conventional Qt 2D transformation matrix that corresponds to this matrix.

The returned :sip:ref:`~PyQt6.QtGui.QTransform` is formed by simply dropping the third row and third column of the :sip:ref:`~PyQt6.QtGui.QMatrix4x4`. This is suitable for implementing orthographic projections where the z co-ordinate should be dropped rather than projected.
