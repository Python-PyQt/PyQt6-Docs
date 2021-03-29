.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 60e76ed0cebeba288c56c69593f13416

Sets the default horizontal and the default vertical spacing for the anchor layout to *spacing*.

If an item is anchored with no spacing associated with the anchor, it will use the default spacing.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout` does not support negative spacings. Setting a negative value will unset the previous spacing and make the layout use the spacing provided by the current widget style.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.setHorizontalSpacing`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.setVerticalSpacing`.
