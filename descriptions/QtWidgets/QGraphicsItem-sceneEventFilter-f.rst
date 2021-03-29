.. sip:method-description::
    :status: todo
    :pysig: eb8e0fcd1b87a03376746f24f3bbd0df
    :realsig: (QGraphicsItem*,QEvent*)
    :digest: 6e1722fe2d8eaa7d17f1f4f0def2dab7

Filters events for the item *watched*. *event* is the filtered event.

Reimplementing this function in a subclass makes it possible for the item to be used as an event filter for other items, intercepting all the events sent to those items before they are able to respond.

Reimplementations must return true to prevent further processing of a given event, ensuring that it will not be delivered to the watched item, or return false to indicate that the event should be propagated further by the event system.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.installSceneEventFilter`.
