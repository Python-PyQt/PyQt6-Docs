.. sip:method-description::
    :status: todo
    :pysig: 7d8f85f92a561a270f248d5d958e81d8
    :realsig: (const QString&,const QFont&)
    :digest: 044657e77998106770701cfb05787e79

Creates and adds a :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem` to the scene, and returns the item pointer. The text string is initialized to *text*, and its font is initialized to *font*.

The item's position is initialized to (0, 0).

If the item is visible (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` returns ``true``), :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will emit :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.changed` once control goes back to the event loop.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addEllipse`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addLine`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addWidget`.
