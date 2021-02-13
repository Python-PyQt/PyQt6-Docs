.. sip:method-description::
    :status: todo
    :pysig: 217764820c56c30ac8085f03823eb57b
    :realsig: (const QRectF&,const QPen&,const QBrush&)
    :digest: 1ff00633173a7c9caa71619c27383f05

Creates and adds an ellipse item to the scene, and returns the item pointer. The geometry of the ellipse is defined by *rect*, and its pen and brush are initialized to *pen* and *brush*.

Note that the item's geometry is provided in item coordinates, and its position is initialized to (0, 0).

If the item is visible (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` returns ``true``), :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will emit :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.changed` once control goes back to the event loop.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addLine`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPath`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addText`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addWidget`.
