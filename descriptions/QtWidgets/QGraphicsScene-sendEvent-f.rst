.. sip:method-description::
    :status: todo
    :pysig: eb8e0fcd1b87a03376746f24f3bbd0df
    :realsig: (QGraphicsItem*,QEvent*)
    :digest: e6bfb77f6de1246855b7cefcce3acf0a

Sends event *event* to item *item* through possible event filters.

The event is sent only if the item is enabled.

Returns ``false`` if the event was filtered or if the item is disabled. Otherwise returns the value that was returned from the event handler.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEventFilter`.
