.. sip:class-description::
    :status: todo
    :brief: Ellipse item that you can add to a QGraphicsScene
    :digest: 2e0a8274bd646af5b65e38103c569e22

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem` class provides an ellipse item that you can add to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem` respresents an ellipse with a fill and an outline, and you can also use it for ellipse segments (see :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem.startAngle`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem.spanAngle`).

+--------------------------------------+------------------------------------------+
| |image-graphicsview-ellipseitem-png| | |image-graphicsview-ellipseitem-pie-png| |
+--------------------------------------+------------------------------------------+

To set the item's ellipse, pass a :sip:ref:`~PyQt6.QtCore.QRectF` to :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`'s constructor, or call :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem.setRect`. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem.rect` function returns the current ellipse geometry.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem` uses the rect and the pen width to provide a reasonable implementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem.shape`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem.contains`. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem.paint` function draws the ellipse using the item's associated pen and brush, which you can set by calling setPen() and setBrush().

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.

.. |image-graphicsview-ellipseitem-png| image:: ../../../images/graphicsview-ellipseitem.png
.. |image-graphicsview-ellipseitem-pie-png| image:: ../../../images/graphicsview-ellipseitem-pie.png
