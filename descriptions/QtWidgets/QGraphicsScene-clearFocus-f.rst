.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 27b30cd4878b8edd2c4c71f2d3c760c7

Clears focus from the scene. If any item has focus when this function is called, it will lose focus, and regain focus again once the scene regains focus.

A scene that does not have focus ignores key events.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.hasFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setFocusItem`.
