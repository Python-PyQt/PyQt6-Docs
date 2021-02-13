.. sip:method-description::
    :status: todo
    :pysig: f7bc0d1799f9addc2f0fc857ce15e6c3
    :realsig: (QVector3D,QVector3D)
    :digest: 12fc9c3e4e28a855b7e9344b120c58a3

Returns the normal vector of a plane defined by vectors *v1* and *v2*, normalized to be a unit vector.

Use :sip:ref:`~PyQt6.QtGui.QVector3D.crossProduct` to compute the cross-product of *v1* and *v2* if you do not need the result to be normalized to a unit vector.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector3D.crossProduct`, :sip:ref:`~PyQt6.QtGui.QVector3D.distanceToPlane`.
