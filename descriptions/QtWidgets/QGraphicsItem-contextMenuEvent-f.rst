.. sip:method-description::
    :status: todo
    :pysig: 6702e72b0e187fd9655ed4b8376208c5
    :realsig: (QGraphicsSceneContextMenuEvent*)
    :digest: e470721e7e912eec328340553e6fb4f9

This event handler can be reimplemented in a subclass to process context menu events. The *event* parameter contains details about the event to be handled.

If you ignore the event (i.e., by calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore`), *event* will propagate to any item beneath this item. If no items accept the event, it will be ignored by the scene and propagate to the view.

It's common to open a :sip:ref:`~PyQt6.QtWidgets.QMenu` in response to receiving a context menu event. Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 196-203

The default implementation ignores the event.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`.
