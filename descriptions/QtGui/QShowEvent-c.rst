.. sip:class-description::
    :status: todo
    :brief: Event that is sent when a widget is shown
    :digest: 661ea83e7cd4142f968a7e3cf6e3e41f

The :sip:ref:`~PyQt6.QtGui.QShowEvent` class provides an event that is sent when a widget is shown.

There are two kinds of show events: show events caused by the window system (spontaneous), and internal show events. Spontaneous (\ :sip:ref:`~PyQt6.QtCore.QEvent.spontaneous`) show events are sent just after the window system shows the window; they are also sent when a top-level window is redisplayed after being iconified. Internal show events are delivered just before the widget becomes visible.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QHideEvent`.
