.. sip:method-description::
    :status: todo
    :pysig: 67a2a7356234c9b932827719146f39eb
    :realsig: (QContextMenuEvent::Reason,const QPoint&,const QPoint&,Qt::KeyboardModifiers)
    :digest: 195beee9d76105247891d38cfb800f3c

Constructs a context menu event object with the accept parameter flag set to false.

The *reason* parameter must be :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.Reason.Mouse` or :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.Reason.Keyboard`.

The *pos* parameter specifies the mouse position relative to the receiving widget. *globalPos* is the mouse position in absolute coordinates. The *modifiers* holds the keyboard modifiers.
