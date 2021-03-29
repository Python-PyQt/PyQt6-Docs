.. sip:method-description::
    :status: todo
    :pysig: 291e9aa8faa22daa13962fd9bee32c5f
    :realsig: (QQuickItem*,QEvent*)
    :digest: bc4b1b3249777d7cef69e2427f663b1b

Reimplement this method to filter the pointer events that are received by this item's children.

This method will only be called if :sip:ref:`~PyQt6.QtQuick.QQuickItem.filtersChildMouseEvents` is ``true``.

Return ``true`` if the specified *event* should not be passed on to the specified child *item*, and ``false`` otherwise.

**Note:** Despite the name, this function filters all :sip:ref:`~PyQt6.QtGui.QPointerEvent` instances during delivery to all children (typically mouse, touch, and tablet events). When overriding this function in a subclass, we suggest writing generic event-handling code using only the accessors found in :sip:ref:`~PyQt6.QtGui.QPointerEvent`. Alternatively you can switch on ``event->type()`` and/or ``event->device()->type()`` to handle different event types in different ways.

**Note:** Filtering is just one way to share responsibility in case of gestural ambiguity (for example on press, you don't know whether the user will tap or drag). Another way is to call QPointerEvent::addPassiveGrabber() on press, so as to non-exclusively monitor the progress of the :sip:ref:`~PyQt6.QtGui.QEventPoint`. In either case, the item or pointer handler that is monitoring can steal the exclusive grab later on, when it becomes clear that the gesture fits the pattern that it is expecting.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickItem.setFiltersChildMouseEvents`.
