.. sip:class-description::
    :status: todo
    :brief: Path item that you can add to a QGraphicsScene
    :digest: f42da8251acc174686c686212f1260cd

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem` class provides a path item that you can add to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`.

To set the item's path, pass a :sip:ref:`~PyQt6.QtGui.QPainterPath` to :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem`'s constructor, or call the :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem.setPath` function. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem.path` function returns the current path.

.. image:: ../../../images/graphicsview-pathitem.png

:sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem` uses the path to provide a reasonable implementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem.shape`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem.contains`. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem.paint` function draws the path using the item's associated pen and brush, which you can set by calling the setPen() and setBrush() functions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.
