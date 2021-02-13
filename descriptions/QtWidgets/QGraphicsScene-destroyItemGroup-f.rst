.. sip:method-description::
    :status: todo
    :pysig: 2587a888abe1145c066322ed566356a2
    :realsig: (QGraphicsItemGroup*)
    :digest: d35ed459edc7e873dedd0a49059e4088

Reparents all items in *group* to *group*'s parent item, then removes *group* from the scene, and finally deletes it. The items' positions and transformations are mapped from the group to the group's parent.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.createItemGroup`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup.removeFromGroup`.
