.. sip:method-description::
    :status: todo
    :pysig: 5da8f1644476e0ef64c9f44891b941e0
    :realsig: (QHoverEvent*)
    :digest: 5ac5f926a392db5a1774651201653038

This event handler can be reimplemented in a subclass to receive hover-move events for an item. The event information is provided by the *event* parameter.

Hover events are only provided if :sip:ref:`~PyQt6.QtQuick.QQuickItem.acceptHoverEvents` is true.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.
