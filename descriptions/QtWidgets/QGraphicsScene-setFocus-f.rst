.. sip:method-description::
    :status: todo
    :pysig: b05f7ab2acd3a40de02d63b859ef1e46
    :realsig: (Qt::FocusReason)
    :digest: ac699b06e2f3c422d678b8c097a9c2f1

Sets focus on the scene by sending a :sip:ref:`~PyQt6.QtGui.QFocusEvent` to the scene, passing *focusReason* as the reason. If the scene regains focus after having previously lost it while an item had focus, the last focus item will receive focus with *focusReason* as the reason.

If the scene already has focus, this function does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.hasFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.clearFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setFocusItem`.
