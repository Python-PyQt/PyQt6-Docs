.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 7202e78ed0ee9e8eb0dd1e121c869728

If *active* is true, and the scene is active, this item's panel will be activated. Otherwise, the panel is deactivated.

If the item is not part of an active scene, *active* will decide what happens to the panel when the scene becomes active or the item is added to the scene. If true, the item's panel will be activated when the item is either added to the scene or the scene is activated. Otherwise, the item will stay inactive independent of the scene's activated state.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isPanel`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setActivePanel`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.isActive`.
