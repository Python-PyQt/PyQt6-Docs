.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 4eb959b81ea68f9dde3047602a808e58

Returns ``true`` if this item is clipped. An item is clipped if it has either set the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemClipsToShape` flag, or if it or any of its ancestors has set the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemClipsChildrenToShape` flag.

Clipping affects the item's appearance (i.e., painting), as well as mouse and hover event delivery.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.clipPath`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.shape`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setFlags`.
