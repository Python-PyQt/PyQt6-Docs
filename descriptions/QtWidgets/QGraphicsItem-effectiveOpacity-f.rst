.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 2147a8fa387dd1d1a18297edd4d019dc

Returns this item's *effective* opacity, which is between 0.0 (transparent) and 1.0 (opaque). This value is a combination of this item's local opacity, and its parent and ancestors' opacities. The effective opacity decides how the item is rendered.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.opacity`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setOpacity`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIgnoresParentOpacity`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemDoesntPropagateOpacityToChildren`.
