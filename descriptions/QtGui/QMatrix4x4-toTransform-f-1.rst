.. sip:method-description::
    :status: todo
    :pysig: 98c2d6964d5776bd9e2dbd827ea194e6
    :realsig: (float) const
    :digest: 2dd0e703321885b0cba8e58bd52ee500

Returns the conventional Qt 2D transformation matrix that corresponds to this matrix.

If *distanceToPlane* is non-zero, it indicates a projection factor to use to adjust for the z co-ordinate. The value of 1024 corresponds to the projection factor used by :sip:ref:`~PyQt6.QtGui.QTransform.rotate` for the x and y axes.

If *distanceToPlane* is zero, then the returned :sip:ref:`~PyQt6.QtGui.QTransform` is formed by simply dropping the third row and third column of the :sip:ref:`~PyQt6.QtGui.QMatrix4x4`. This is suitable for implementing orthographic projections where the z co-ordinate should be dropped rather than projected.
