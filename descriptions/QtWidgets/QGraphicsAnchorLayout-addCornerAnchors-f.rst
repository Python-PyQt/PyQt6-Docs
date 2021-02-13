.. sip:method-description::
    :status: todo
    :pysig: 349ac5ed04ca6aaca14390a60e460e87
    :realsig: (QGraphicsLayoutItem*,Qt::Corner,QGraphicsLayoutItem*,Qt::Corner)
    :digest: 462b8e6c6705d363e678b751f77d46c7

Creates two anchors between *firstItem* and *secondItem* specified by the corners, *firstCorner* and *secondCorner*, where one is for the horizontal edge and another one for the vertical edge.

This is a convenience function, since anchoring corners can be expressed as anchoring two edges. For instance:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-graphicsview-simpleanchorlayout-main.py
    :lines: 102-103

This can also be achieved with the following line of code:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-graphicsview-simpleanchorlayout-main.py
    :lines: 107-107

If there is already an anchor between the edge pairs, it will be replaced by the anchors that this function specifies.

*firstItem* and *secondItem* are automatically added to the layout if they are not part of the layout. This means that :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.count` can increase by up to 2.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addAnchor`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addAnchors`.
