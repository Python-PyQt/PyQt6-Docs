.. sip:method-description::
    :status: todo
    :pysig: 28603bc6d1982279eeb15ba34f0d1eb4
    :realsig: (QGraphicsLayoutItem*,QGraphicsLayoutItem*,Qt::Orientations)
    :digest: 9514adebf3be4b8e48d40e904fcaa25f

Anchors two or four edges of *firstItem* with the corresponding edges of *secondItem*, so that *firstItem* has the same size as *secondItem* in the dimensions specified by *orientations*.

For example, the following example anchors the left and right edges of two items to match their widths:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-graphicsview-simpleanchorlayout-main.py
    :lines: 120-121

This can also be achieved using the following line of code:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-graphicsview-simpleanchorlayout-main.py
    :lines: 126-126

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addAnchor`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addCornerAnchors`.
