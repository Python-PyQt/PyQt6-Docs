.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: () const
    :digest: 15fc9891d27a9aed350b062ba93543ac

Returns the bounding rect of this item's descendants (i.e., its children, their children, etc.) in local coordinates. The rectangle will contain all descendants after they have been mapped to local coordinates. If the item has no children, this function returns an empty :sip:ref:`~PyQt6.QtCore.QRectF`.

This does not include this item's own bounding rect; it only returns its descendants' accumulated bounding rect. If you need to include this item's bounding rect, you can add :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect` to  using QRectF::operator|().

This function is linear in complexity; it determines the size of the returned bounding rect by iterating through all descendants.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneBoundingRect`.
