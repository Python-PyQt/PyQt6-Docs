.. sip:method-description::
    :status: todo
    :pysig: 4340370960e4369d296c631a9d32cdfb
    :realsig: (const QPolygon&) const
    :digest: 81ce4e6a9b3a3b44780efd2295b4f652

Returns ``true`` if the current polygon intersects at any point the given polygon *p*. Also returns ``true`` if the current polygon contains or is contained by any part of *p*.

Set operations on polygons will treat the polygons as areas. Non-closed polygons will be treated as implicitly closed.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPolygon.intersected`.
