.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 6559189edb2473f121407c3c51fe2119

Sets the scale *factor* of the item. The default scale factor is 1.0 (i.e., the item is not scaled). A scale factor of 0.0 will collapse the item to a single point. If you provide a negative scale factor, the item will be flipped and mirrored (i.e., rotated 180 degrees).

The item is scaled around its transform origin point, which by default is (0, 0). You can select a different transformation origin by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformOriginPoint`.

The scale is combined with the item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.rotation`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transformations` to map the item's coordinate system to the parent item.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scale`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransformOriginPoint`, `Transformations Example <https://doc.qt.io/qt-6/qtwidgets-painting-transformations-example.html>`_.
