.. sip:method-description::
    :status: todo
    :pysig: 4bc45bd1f0f96cc03e6c09d2fb033be2
    :realsig: (QVector3D,QVector3D,QVector3D)
    :digest: 10939f86f5cce20ceba72903cc6f8ee3

Returns the unit normal vector of a plane spanned by vectors *v2* - *v1* and *v3* - *v1*, which must not be parallel to one another.

Use :sip:ref:`~PyQt6.QtGui.QVector3D.crossProduct` to compute the cross-product of *v2* - *v1* and *v3* - *v1* if you do not need the result to be normalized to a unit vector.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector3D.crossProduct`, :sip:ref:`~PyQt6.QtGui.QVector3D.distanceToPlane`.
