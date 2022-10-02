.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 0ca11d77bc963405ffd5b21de48abe28

If *enabled* is true, the item is enabled; otherwise, it is disabled.

Disabled items are visible, but they do not receive any events, and cannot take focus nor be selected. Mouse events are discarded; they are not propagated unless the item is also invisible, or if it does not accept mouse events (see :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.acceptedMouseButtons`). A disabled item cannot become the mouse grabber, and as a result of this, an item loses the grab if it becomes disabled when grabbing the mouse, just like it loses focus if it had focus when it was disabled.

Disabled items are traditionally drawn using grayed-out colors (see :sip:ref:`~PyQt6.QtGui.QPalette.ColorGroup.Disabled`).

If you disable a parent item, all its children will also be disabled. If you enable a parent item, all children will be enabled, unless they have been explicitly disabled (i.e., if you call setEnabled(false) on a child, it will not be re-enabled if its parent is disabled, and then enabled again).

Items are enabled by default.

**Note:** If you install an event filter, you can still intercept events before they are delivered to items; this mechanism disregards the item's enabled state.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isEnabled`.
