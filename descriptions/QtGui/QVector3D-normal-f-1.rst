.. sip:method-description::
    :status: todo
    :pysig: 4bc45bd1f0f96cc03e6c09d2fb033be2
    :realsig: (QVector3D,QVector3D,QVector3D)
    :digest: 923ddb2d414b192083f0d914d8f20b26

Returns the normal vector of a plane defined by vectors *v2* - *v1* and *v3* - *v1*, normalized to be a unit vector.

Use :sip:ref:`~PyQt6.QtGui.QVector3D.crossProduct` to compute the cross-product of *v2* - *v1* and *v3* - *v1* if you do not need the result to be normalized to a unit vector.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector3D.crossProduct`, :sip:ref:`~PyQt6.QtGui.QVector3D.distanceToPlane`.
