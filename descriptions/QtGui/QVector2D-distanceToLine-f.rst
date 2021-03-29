.. sip:method-description::
    :status: todo
    :pysig: 4de759fc5d5e238821c1b728df575a04
    :realsig: (QVector2D,QVector2D) const
    :digest: 7bafca5fad76c6b110acd1b663fc8f4f

Returns the distance that this vertex is from a line defined by *point* and the unit vector *direction*.

If *direction* is a null vector, then it does not define a line. In that case, the distance from *point* to this vertex is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector2D.distanceToPoint`.
