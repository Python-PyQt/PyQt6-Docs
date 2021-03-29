.. sip:method-description::
    :status: todo
    :pysig: c37006bda2f9fa352b6dbcaf52ec954b
    :realsig: (const QPainterPath&,Qt::ItemSelectionOperation,Qt::ItemSelectionMode,const QTransform&)
    :digest: d390275eff710da6992317de1e5d1503

This is an overloaded function.

Sets the selection area to *path* using *mode* to determine if items are included in the selection area.

*deviceTransform* is the transformation that applies to the view, and needs to be provided if the scene contains items that ignore transformations.

*selectionOperation* determines what to do with the currently selected items.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.clearSelection`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.selectionArea`.
