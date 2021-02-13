.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: (QGraphicsItem*)
    :digest: fae21388fe2b7c45d91a5fd43c703b92

Adds or moves the *item* and all its childen to this scene. This scene takes ownership of the *item*.

If the item is visible (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isVisible` returns true), :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will emit :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.changed` once control goes back to the event loop.

If the item is already in a different scene, it will first be removed from its old scene, and then added to this scene as a top-level.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will send ItemSceneChange notifications to *item* while it is added to the scene. If item does not currently belong to a scene, only one notification is sent. If it does belong to scene already (i.e., it is moved to this scene), :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` will send an addition notification as the item is removed from its previous scene.

If the item is a panel, the scene is active, and there is no active panel in the scene, then the item will be activated.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.removeItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addEllipse`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addLine`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPath`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addPixmap`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addText`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addWidget`, Sorting.
