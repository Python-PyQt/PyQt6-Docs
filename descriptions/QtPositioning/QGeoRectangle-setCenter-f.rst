.. sip:method-description::
    :status: todo
    :pysig: 1d70d2f718748a9d33eeeaebd82dd1eb
    :realsig: (const QGeoCoordinate&)
    :digest: 395438dd3a56eae341851f026717d0fe

Sets the center of this geo rectangle to *center*.

If this causes the geo rectangle to cross on of the poles the height of the geo rectangle will be truncated such that the geo rectangle only extends up to the pole. The center of the geo rectangle will be unchanged, and the height will be adjusted such that the center point is at the center of the truncated geo rectangle.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoRectangle.center`.
