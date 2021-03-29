.. sip:method-description::
    :status: todo
    :pysig: 06402b162572f668d054f99bc1104063
    :realsig: (const QGraphicsItem*) const
    :digest: 1365639d823cebab61ffd270a2920027

Returns ``true`` if this item's bounding rect is completely obscured by the opaque shape of *item*.

The base implementation maps *item*'s :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.opaqueArea` to this item's coordinate system, and then checks if this item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect` is fully contained within the mapped shape.

You can reimplement this function to provide a custom algorithm for determining whether this item is obscured by *item*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.opaqueArea`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isObscured`.
