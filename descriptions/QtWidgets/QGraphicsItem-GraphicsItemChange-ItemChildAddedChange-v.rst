.. sip:enum-member-description::
    :status: todo
    :value: 6
    :digest: 37345f2ec2d9d217f3fbef607aa9ca29

A child is added to this item. The value argument is the new child item (i.e., a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` pointer). Do not pass this item to any item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setParentItem` function as this notification is delivered. The return value is unused; you cannot adjust anything in this notification. Note that the new child might not be fully constructed when this notification is sent; calling pure virtual functions on the child can lead to a crash.
