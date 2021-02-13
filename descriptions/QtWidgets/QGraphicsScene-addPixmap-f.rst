.. sip:method-description::
    :status: todo
    :pysig: 66ce12cd227689738fd4e41a4ea6014e
    :realsig: (const QPixmap&)
    :digest: e4145872142a626209d0b9bc41e589cf

Creates and adds a pixmap item to the scene, and returns the item pointer. The pixmap is defined by *pixmap*.

Note that the item's geometry is provided in item coordinates, and its position is initialized to (0, 0).

If the item is visible (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` returns ``true``), :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will emit :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.changed` once control goes back to the event loop.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addEllipse`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addLine`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPath`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addText`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addWidget`.
