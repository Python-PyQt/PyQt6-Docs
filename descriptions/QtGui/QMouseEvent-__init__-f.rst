.. sip:method-description::
    :status: todo
    :pysig: 5d808367668db5f1014cea49a147bb6f
    :realsig: (QEvent::Type,const QPointF&,Qt::MouseButton,Qt::MouseButtons,Qt::KeyboardModifiers,const QPointingDevice*)
    :digest: 152b32d2cb818dbf940f9330ca05209e

Constructs a mouse event object originating from *device*.

The *type* parameter must be one of :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonPress`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonRelease`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonDblClick`, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseMove`.

The *localPos* is the mouse cursor's position relative to the receiving widget or item. The window position is set to the same value as *localPos*. The *button* that caused the event is given as a value from the :sip:ref:`~PyQt6.QtCore.Qt.MouseButtons` enum. If the event *type* is :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseMove`, the appropriate button for this event is :sip:ref:`~PyQt6.QtCore.Qt.MouseButtons.NoButton`. The mouse and keyboard states at the time of the event are specified by *buttons* and *modifiers*.

The globalPosition() is initialized to :sip:ref:`~PyQt6.QtGui.QCursor.pos`, which may not be appropriate. Use the other constructor to specify the global position explicitly.
