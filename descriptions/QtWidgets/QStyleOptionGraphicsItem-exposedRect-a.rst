.. sip:attribute-description::
    :status: todo
    :digest: 9c7598ffc046e7ba3168c1c0967fca42

This variable holds the exposed rectangle, in item coordinates.

Make use of this rectangle to speed up item drawing when only parts of the item are exposed. If the whole item is exposed, this rectangle will be the same as :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`.

This member is only initialized for items that have the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemUsesExtendedStyleOption` flag set.
