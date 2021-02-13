.. sip:method-description::
    :status: todo
    :pysig: bd215c77244bcb680eac9c452b1494f6
    :realsig: (QGraphicsLayoutItem*,Qt::AnchorPoint,QGraphicsLayoutItem*,Qt::AnchorPoint)
    :digest: 93f70cb090f7e7e01d9d3cae4a22f770

Creates an anchor between the edge *firstEdge* of item *firstItem* and the edge *secondEdge* of item *secondItem*. The spacing of the anchor is picked up from the style. Anchors between a layout edge and an item edge will have a size of 0. If there is already an anchor between the edges, the new anchor will replace the old one.

*firstItem* and *secondItem* are automatically added to the layout if they are not part of the layout. This means that :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.count` can increase by up to 2.

The spacing an anchor will get depends on the type of anchor. For instance, anchors from the Right edge of one item to the Left edge of another (or vice versa) will use the default horizontal spacing. The same behaviour applies to Bottom to Top anchors, (but they will use the default vertical spacing). For all other anchor combinations, the spacing will be 0. All anchoring functions will follow this rule.

The spacing can also be set manually by using :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchor.setSpacing` method.

Calling this function where *firstItem* or *secondItem* are ancestors of the layout have undefined behaviour.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addAnchors`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addCornerAnchors`.
