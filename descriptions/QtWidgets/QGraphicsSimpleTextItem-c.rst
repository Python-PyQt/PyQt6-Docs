.. sip:class-description::
    :status: todo
    :brief: Simple text item that you can add to a QGraphicsScene
    :digest: 83c41b4d7b83c61b180a4f17adb2a2c0

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem` class provides a simple text item that you can add to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`.

To set the item's text, you can either pass a QString to :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem`'s constructor, or call :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem.setText` to change the text later. To set the text fill color, call setBrush().

The simple text item can have both a fill and an outline; setBrush() will set the text fill (i.e., text color), and setPen() sets the pen that will be used to draw the text outline. (The latter can be slow, especially for complex pens, and items with long text content.) If all you want is to draw a simple line of text, you should call setBrush() only, and leave the pen unset; :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem`'s pen is by default :sip:ref:`~PyQt6.QtCore.Qt.PenStyle.NoPen`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem` uses the text's formatted size and the associated font to provide a reasonable implementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem.shape`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem.contains`. You can set the font by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem.setFont`.

QGraphicsSimpleText does not display rich text; instead, you can use :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`, which provides full text control capabilities.

.. image:: ../../../images/graphicsview-simpletextitem.png

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.
