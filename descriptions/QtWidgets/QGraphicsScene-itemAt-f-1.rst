.. sip:method-description::
    :status: todo
    :pysig: cf2ec177d8144660a5a1f6597034eac0
    :realsig: (qreal,qreal,const QTransform&) const
    :digest: d96165181ee240aaa567df9fdc26fcf3

Returns the topmost visible item at the position specified by (\ *x*, *y*), or ``nullptr`` if there are no items at this position.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.

This convenience function is equivalent to calling ``itemAt(QPointF(x, y), deviceTransform)``.

Note: See :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items` for a definition of which items are considered visible by this function.
