.. sip:method-description::
    :status: todo
    :pysig: a28d7c815182564df2c1abd853ad768a
    :realsig: (QFocusEvent*)
    :digest: 811716697efe7282b6a8a15b2b82bb4c

This event handler, for event *focusEvent*, can be reimplemented in a subclass to receive focus out events.

The default implementation removes focus from any focus item, then removes focus from the scene.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.focusInEvent`.
