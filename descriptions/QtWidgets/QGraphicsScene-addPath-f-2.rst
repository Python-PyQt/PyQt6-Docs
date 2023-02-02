.. sip:method-description::
    :status: todo
    :pysig: 6482133cc78760192144dd0c6984e150
    :realsig: (const QPainterPath&,const QPen&,const QBrush&)
    :digest: 63980d2f6c56faf78b0d45d0af859c42

Creates and adds a path item to the scene, and returns the item pointer. The geometry of the path is defined by *path*, and its pen and brush are initialized to *pen* and *brush*.

Note that the item's geometry is provided in item coordinates, and its position is initialized to (0, 0).

If the item is visible (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` returns ``true``), :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will emit :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.changed` once control goes back to the event loop.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addEllipse`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addLine`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addText`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addWidget`.
