.. sip:method-description::
    :status: todo
    :pysig: e76d867df34704d8edf43af1cfd337bd
    :realsig: (QGraphicsSceneHelpEvent*)
    :digest: c7022c524af677b3d93156c0c1b68908

This event handler, for event *helpEvent*, can be reimplemented in a subclass to receive help events. The events are of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.ToolTip`, which are created when a tooltip is requested.

The default implementation shows the tooltip of the topmost visible item, i.e., the item with the highest z-value, at the mouse cursor position. If no item has a tooltip set, this function does nothing.

Note: See :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items` for a definition of which items are considered visible by this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.toolTip`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneHelpEvent`.
