.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: (QGraphicsItem*)
    :digest: 53d335b1359af84e8133ae8ce310e1c7

Activates *item*, which must be an item in this scene. You can also pass 0 for *item*, in which case :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will deactivate any currently active panel.

If the scene is currently inactive, *item* remains inactive until the scene becomes active (or, ir *item* is ``nullptr``, no item will be activated).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.activePanel`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.isActive`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isActive`.
