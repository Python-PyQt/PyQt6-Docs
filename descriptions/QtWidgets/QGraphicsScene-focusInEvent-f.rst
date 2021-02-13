.. sip:method-description::
    :status: todo
    :pysig: a28d7c815182564df2c1abd853ad768a
    :realsig: (QFocusEvent*)
    :digest: ed24847b2077296f356a6cc02debcfcf

This event handler, for event *focusEvent*, can be reimplemented in a subclass to receive focus in events.

The default implementation sets focus on the scene, and then on the last focus item.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.focusOutEvent`.
