.. sip:method-description::
    :status: todo
    :pysig: b1168915c328c8447b830caea22759a0
    :realsig: (QGraphicsSceneResizeEvent*)
    :digest: 9245d8535e16d178e8e06dc454a7d1d8

This event handler, for :sip:ref:`~PyQt6.QtCore.QEvent.Type.GraphicsSceneResize` events, is delivered after the widget has been resized (i.e., its local size has changed). *event* contains both the old and the new size.

This event is only delivered when the widget is resized locally; calling setTransform() on the widget or any of its ancestors or view, does not affect the widget's local size.

You can reimplement this event handler to detect when your widget has been resized. Calling :sip:ref:`~PyQt6.QtCore.QEvent.accept` or :sip:ref:`~PyQt6.QtCore.QEvent.ignore` on *event* has no effect.

.. seealso:: geometry(), :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.setGeometry`.
