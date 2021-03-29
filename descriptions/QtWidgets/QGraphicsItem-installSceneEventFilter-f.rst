.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: (QGraphicsItem*)
    :digest: 1a99b95e7c00c1a4642813708e31ad60

Installs an event filter for this item on *filterItem*, causing all events for this item to first pass through *filterItem*'s :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEventFilter` function.

To filter another item's events, install this item as an event filter for the other item. Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 183-191

An item can only filter events for other items in the same scene. Also, an item cannot filter its own events; instead, you can reimplement :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent` directly.

Items must belong to a scene for scene event filters to be installed and used.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.removeSceneEventFilter`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEventFilter`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`.
