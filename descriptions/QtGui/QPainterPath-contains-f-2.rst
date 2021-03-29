.. sip:method-description::
    :status: todo
    :pysig: 063b4bd94a2c6c9a999b20cc06cd4567
    :realsig: (const QPainterPath&) const
    :digest: cc46c12219d2d51e4af68a67c5523cbf

Returns ``true`` if the given path *p* is contained within the current path. Returns ``false`` if any edges of the current path and *p* intersect.

Set operations on paths will treat the paths as areas. Non-closed paths will be treated as implicitly closed.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.intersects`.
