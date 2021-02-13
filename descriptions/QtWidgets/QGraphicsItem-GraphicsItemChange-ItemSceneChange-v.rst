.. sip:enum-member-description::
    :status: todo
    :value: 11
    :digest: c1cc67b5a39abae3671cb82db2c60f6e

The item is moved to a new scene. This notification is also sent when the item is added to its initial scene, and when it is removed. The item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.scene` is the old scene, or ``nullptr`` if the item has not been added to a scene yet. The value argument is the new scene (i.e., a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` pointer), or ``nullptr`` if the item is removed from a scene. Do not override this change by passing this item to :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addItem` as this notification is delivered; instead, you can return the new scene from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`. Use this feature with caution; objecting to a scene change can quickly lead to unwanted recursion.
