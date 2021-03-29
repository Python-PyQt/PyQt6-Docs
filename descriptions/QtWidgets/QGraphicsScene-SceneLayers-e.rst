.. sip:enum-description::
    :status: todo
    :realname: QGraphicsScene::SceneLayer
    :digest: 273cd763880a0d2f2c0ff0cf163dedb3

This enum describes the rendering layers in a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`. When :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` draws the scene contents, it renders each of these layers separately, in order.

Each layer represents a flag that can be OR'ed together when calling functions such as :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.invalidate` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.invalidateScene`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.invalidate`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.invalidateScene`.
