.. sip:method-description::
    :status: todo
    :pysig: 4490a8d0e22b4e949f8cc6cb75745cd0
    :realsig: (const QPolygonF&) const
    :digest: 8308b97a95c565c75ed82fe466c01e69

Returns a polygon which is the union of this polygon and *r*.

Set operations on polygons will treat the polygons as areas. Non-closed polygons will be treated as implicitly closed.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPolygonF.intersected`, :sip:ref:`~PyQt6.QtGui.QPolygonF.subtracted`.
