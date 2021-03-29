.. sip:method-description::
    :status: todo
    :pysig: b53df27f41e7e1e87eded6e72ecfdeb9
    :realsig: () const
    :digest: 7eed2e8f3b98f3b668227ff8f0504c94

Returns this item's clip path, or an empty :sip:ref:`~PyQt6.QtGui.QPainterPath` if this item is not clipped. The clip path constrains the item's appearance and interaction (i.e., restricts the area the item can draw within and receive events for).

You can enable clipping by setting the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemClipsToShape` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemClipsChildrenToShape` flags. The item's clip path is calculated by intersecting all clipping ancestors' shapes. If the item sets :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemClipsToShape`, the final clip is intersected with the item's own shape.

**Note:** Clipping introduces a performance penalty for all items involved; you should generally avoid using clipping if you can (e.g., if your items always draw inside :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape` boundaries, clipping is not necessary).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isClipped`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setFlags`.
