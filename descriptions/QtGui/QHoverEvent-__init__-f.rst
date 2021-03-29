.. sip:method-description::
    :status: todo
    :pysig: d3a40dd5018cf0bd70eb2a21fbf40146
    :realsig: (QEvent::Type,const QPointF&,const QPointF&,Qt::KeyboardModifiers,const QPointingDevice*)
    :digest: 3bc5fb8b0c5976117881a77cdbbd460f

Constructs a hover event object originating from *device*.

The *type* parameter must be :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverEnter`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverLeave`, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverMove`.

The *pos* is the current mouse cursor's position relative to the receiving widget, while *oldPos* is its previous such position. *modifiers* hold the state of all keyboard modifiers at the time of the event.
