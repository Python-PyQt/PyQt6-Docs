.. sip:method-description::
    :status: todo
    :pysig: d44a710c000db38a04264ffb04a16396
    :realsig: (QVector3D,QVector3D) const
    :digest: 3ccc983e0e7d9d196a89d51b850a2788

Returns the distance that this vertex is from a line defined by *point* and the unit vector *direction*.

If *direction* is a null vector, then it does not define a line. In that case, the distance from *point* to this vertex is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector3D.distanceToPlane`.
