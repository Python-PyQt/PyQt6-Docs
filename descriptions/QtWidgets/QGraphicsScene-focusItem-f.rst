.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: () const
    :digest: a65178b46140200e89b448c3cc7e3291

When the scene is active, this functions returns the scene's current focus item, or ``nullptr`` if no item currently has focus. When the scene is inactive, this functions returns the item that will gain input focus when the scene becomes active.

The focus item receives keyboard input when the scene receives a key event.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setFocusItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hasFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.isActive`.
