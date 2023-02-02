.. sip:method-description::
    :status: todo
    :pysig: 78b5bee8d190804990a466d6951b8353
    :realsig: (const QRectF&,const QPen&,const QBrush&)
    :digest: 988f2ed37202db1daf879d196147cf1c

Creates and adds a rectangle item to the scene, and returns the item pointer. The geometry of the rectangle is defined by *rect*, and its pen and brush are initialized to *pen* and *brush*.

Note that the item's geometry is provided in item coordinates, and its position is initialized to (0, 0). For example, if a :sip:ref:`~PyQt6.QtCore.QRect`\ (50, 50, 100, 100) is added, its top-left corner will be at (50, 50) relative to the origin in the item's coordinate system.

If the item is visible (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` returns ``true``), :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will emit :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.changed` once control goes back to the event loop.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addEllipse`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addLine`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addText`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addWidget`.
