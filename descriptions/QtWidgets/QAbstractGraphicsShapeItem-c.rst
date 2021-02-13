.. sip:class-description::
    :status: todo
    :brief: Common base for all path items
    :digest: 6d9ab3bf2ac910c1d18d341ea0775c2e

The :sip:ref:`~PyQt6.QtWidgets.QAbstractGraphicsShapeItem` class provides a common base for all path items.

This class does not fully implement an item by itself; in particular, it does not implement boundingRect() and paint(), which are inherited by :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`.

You can subclass this item to provide a simple base implementation of accessors for the item's pen and brush.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.
