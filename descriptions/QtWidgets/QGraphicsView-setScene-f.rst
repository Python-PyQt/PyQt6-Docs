.. sip:method-description::
    :status: todo
    :pysig: 09283cd761d555cc89fef5213fa4d536
    :realsig: (QGraphicsScene*)
    :digest: 9fc483eaad3a0ab6614ddc443e9c70da

Sets the current scene to *scene*. If *scene* is already being viewed, this function does nothing.

When a scene is set on a view, the :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.changed` signal is automatically connected to this view's :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.updateScene` slot, and the view's scroll bars are adjusted to fit the size of the scene.

The view does not take ownership of *scene*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.scene`.
