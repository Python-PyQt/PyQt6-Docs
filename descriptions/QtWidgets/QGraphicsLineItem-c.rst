.. sip:class-description::
    :status: todo
    :brief: Line item that you can add to a QGraphicsScene
    :digest: 8ac57e40419de7744526178129f798dd

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem` class provides a line item that you can add to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`.

To set the item's line, pass a :sip:ref:`~PyQt6.QtCore.QLineF` to :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`'s constructor, or call the :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem.setLine` function. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem.line` function returns the current line. By default the line is black with a width of 0, but you can change this by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem.setPen`.

.. image:: ../../../images/graphicsview-lineitem.png

:sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem` uses the line and the pen width to provide a reasonable implementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem.shape`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem.contains`. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem.paint` function draws the line using the item's associated pen.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.
