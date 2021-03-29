.. sip:class-description::
    :status: todo
    :brief: Polygon item that you can add to a QGraphicsScene
    :digest: 69449b4963f836304943744f1cf7de18

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem` class provides a polygon item that you can add to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`.

To set the item's polygon, pass a :sip:ref:`~PyQt6.QtGui.QPolygonF` to :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem`'s constructor, or call the :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem.setPolygon` function. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem.polygon` function returns the current polygon.

.. image:: ../../../images/graphicsview-polygonitem.png

:sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem` uses the polygon and the pen width to provide a reasonable implementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem.shape`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem.contains`. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem.paint` function draws the polygon using the item's associated pen and brush, which you can set by calling the setPen() and setBrush() functions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.
