.. sip:method-description::
    :status: todo
    :pysig: 79c3e2b05f1ff4c925ac57da426b0d74
    :realsig: (QEvent::Type,const QPointF&,const QPointF&,const QPointF&,Qt::MouseButton,Qt::MouseButtons,Qt::KeyboardModifiers,const QPointingDevice*)
    :digest: 7110bf03ed49452244d81f818689a839

Constructs a mouse event object.

The *type* parameter must be :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonPress`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonRelease`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonDblClick`, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseMove`.

The points *localPos*, *scenePos* and *globalPos* specify the mouse cursor's position relative to the receiving widget or item, window, and screen or desktop, respectively.

The *button* that caused the event is given as a value from the :sip:ref:`~PyQt6.QtCore.Qt.MouseButtons` enum. If the event *type* is :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseMove`, the appropriate button for this event is :sip:ref:`~PyQt6.QtCore.Qt.MouseButtons.NoButton`. *buttons* is the state of all buttons at the time of the event, *modifiers* is the state of all keyboard modifiers.
