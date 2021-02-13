.. sip:method-description::
    :status: todo
    :pysig: 18454bf1e49bbcc575a29fd6551a2166
    :realsig: (QEvent::Type,const QPointF&,const QPointF&,Qt::MouseButton,Qt::MouseButtons,Qt::KeyboardModifiers,const QPointingDevice*)
    :digest: 9c27eabc7711053e6e5de22507747664

Constructs a mouse event object originating from *device*.

The *type* parameter must be :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonPress`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonRelease`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonDblClick`, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseMove`.

The *localPos* is the mouse cursor's position relative to the receiving widget or item. The cursor's position in screen coordinates is specified by *globalPos*. The window position is set to the same value as *localPos*. The *button* that caused the event is given as a value from the :sip:ref:`~PyQt6.QtCore.Qt.MouseButtons` enum. If the event *type* is :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseMove`, the appropriate button for this event is :sip:ref:`~PyQt6.QtCore.Qt.MouseButtons.NoButton`. *buttons* is the state of all buttons at the time of the event, *modifiers* the state of all keyboard modifiers.
