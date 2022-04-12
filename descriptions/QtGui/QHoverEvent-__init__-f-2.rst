.. sip:method-description::
    :status: todo
    :pysig: 88980cffd0a8c721f9d8bf46738b8a7e
    :realsig: (QEvent::Type,const QPointF&,const QPointF&,const QPointF&,Qt::KeyboardModifiers,const QPointingDevice*)
    :digest: 8f15933b7eb5459547e5433213a148ec

Constructs a hover event object originating from *device*.

The *type* parameter must be :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverEnter`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverLeave`, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverMove`.

The *pos* is the current mouse cursor's position relative to the receiving widget, *oldPos* is its previous such position, and *globalPos* is the mouse position in absolute coordinates. *modifiers* hold the state of all keyboard modifiers at the time of the event.
