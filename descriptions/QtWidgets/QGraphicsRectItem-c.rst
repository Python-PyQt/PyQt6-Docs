.. sip:class-description::
    :status: todo
    :brief: Rectangle item that you can add to a QGraphicsScene
    :digest: 9c5b257d53a5478ab928daef4128c2f4

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem` class provides a rectangle item that you can add to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`.

To set the item's rectangle, pass a :sip:ref:`~PyQt6.QtCore.QRectF` to :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`'s constructor, or call the :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem.setRect` function. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem.rect` function returns the current rectangle.

.. image:: ../../../images/graphicsview-rectitem.png

:sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem` uses the rectangle and the pen width to provide a reasonable implementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem.shape`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem.contains`. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem.paint` function draws the rectangle using the item's associated pen and brush, which you can set by calling the setPen() and setBrush() functions.

**Note:** The rendering of invalid rectangles, such as those with negative widths or heights, is undefined. If you cannot be sure that you are using valid rectangles (for example, if you are creating rectangles using data from an unreliable source) then you should use :sip:ref:`~PyQt6.QtCore.QRectF.normalized` to create normalized rectangles, and use those instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.
