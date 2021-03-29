.. sip:method-description::
    :status: todo
    :pysig: cf2ec177d8144660a5a1f6597034eac0
    :realsig: (qreal,qreal,const QTransform&) const
    :digest: 3228b188853c38e5a170792cbb578a53

This is an overloaded function.

Returns the topmost visible item at the position specified by (\ *x*, *y*), or ``nullptr`` if there are no items at this position.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.

This convenience function is equivalent to calling ``itemAt(QPointF(x, y), deviceTransform)``.

Note: See :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items` for a definition of which items are considered visible by this function.
