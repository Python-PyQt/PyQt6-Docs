.. sip:method-description::
    :status: todo
    :pysig: f7bc0d1799f9addc2f0fc857ce15e6c3
    :realsig: (QVector3D,QVector3D)
    :digest: b3635bd6ac391ccf8f78968e8ba6ee85

Returns the unit normal vector of a plane spanned by vectors *v1* and *v2*, which must not be parallel to one another.

Use :sip:ref:`~PyQt6.QtGui.QVector3D.crossProduct` to compute the cross-product of *v1* and *v2* if you do not need the result to be normalized to a unit vector.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector3D.crossProduct`, :sip:ref:`~PyQt6.QtGui.QVector3D.distanceToPlane`.
