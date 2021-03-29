.. sip:class-description::
    :status: todo
    :brief: Text item that you can add to a QGraphicsScene to display formatted text
    :digest: 6ebb9a41a8bdd172d759368ccd249e35

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem` class provides a text item that you can add to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` to display formatted text.

If you only need to show plain text in an item, consider using :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem` instead.

To set the item's text, pass a QString to :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`'s constructor, or call :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.setHtml`/\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.setPlainText`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem` uses the text's formatted size and the associated font to provide a reasonable implementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.shape`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.contains`. You can set the font by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.setFont`.

It is possible to make the item editable by setting the :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlags.TextEditorInteraction` flag using :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.setTextInteractionFlags`.

The item's preferred text width can be set using :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.setTextWidth` and obtained using :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.textWidth`.

**Note:** In order to align HTML text in the center, the item's text width must be set. Otherwise, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.adjustSize` after setting the item's text.

.. image:: ../../../images/graphicsview-textitem.png

**Note:** :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem` accepts :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.acceptHoverEvents` by default. You can change this with :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptHoverEvents`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.
