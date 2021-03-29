.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a touch event
    :digest: 9a14b794fc82f31d6f452f3af2e098d4

The :sip:ref:`~PyQt6.QtGui.QTouchEvent` class contains parameters that describe a touch event.

.. _qtouchevent-enabling-touch-events:

Enabling Touch Events
---------------------

Touch events occur when pressing, releasing, or moving one or more touch points on a touch device (such as a touch-screen or track-pad). To receive touch events, widgets have to have the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_AcceptTouchEvents` attribute set and graphics items need to have the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptTouchEvents` attribute set to true.

When using :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` based widgets, you should enable the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_AcceptTouchEvents` attribute on the scroll area's :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.viewport`.

Similarly to :sip:ref:`~PyQt6.QtGui.QMouseEvent`, Qt automatically grabs each touch point on the first press inside a widget, and the widget will receive all updates for the touch point until it is released. Note that it is possible for a widget to receive events for numerous touch points, and that multiple widgets may be receiving touch events at the same time.

.. _qtouchevent-event-handling:

Event Handling
--------------

All touch events are of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchBegin`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchUpdate`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchEnd` or :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchCancel`. Reimplement :sip:ref:`~PyQt6.QtWidgets.QWidget.event` or :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.viewportEvent` for widgets and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent` for items in a graphics view to receive touch events.

Unlike widgets, QWindows receive touch events always, there is no need to opt in. When working directly with a :sip:ref:`~PyQt6.QtGui.QWindow`, it is enough to reimplement :sip:ref:`~PyQt6.QtGui.QWindow.touchEvent`.

The :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchUpdate` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchEnd` events are sent to the widget or item that accepted the :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchBegin` event. If the :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchBegin` event is not accepted and not filtered by an event filter, then no further touch events are sent until the next :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchBegin`.

Some systems may send an event of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchCancel`. Upon receiving this event applications are requested to ignore the entire active touch sequence. For example in a composited system the compositor may decide to treat certain gestures as system-wide gestures. Whenever such a decision is made (the gesture is recognized), the clients will be notified with a :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchCancel` event so they can update their state accordingly.

The pointCount() and point() functions can be used to access and iterate individual touch points.

The  function returns a list of all touch points contained in the event. Note that this list may be empty, for example in case of a :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchCancel` event. Each point is an instance of the :sip:ref:`~PyQt6.QtGui.QEventPoint` class. The :sip:ref:`~PyQt6.QtGui.QEventPoint.States` enum describes the different states that a touch point may have.

**Note:** The list of  will never be partial: A touch event will always contain a touch point for each existing physical touch contacts targetting the window or widget to which the event is sent. For instance, assuming that all touches target the same window or widget, an event with a condition of .count()==2 is guaranteed to imply that the number of fingers touching the touchscreen or touchpad is exactly two.

.. _qtouchevent-event-delivery-and-propagation:

Event Delivery and Propagation
------------------------------

By default, :sip:ref:`~PyQt6.QtGui.QGuiApplication` translates the first touch point in a :sip:ref:`~PyQt6.QtGui.QTouchEvent` into a :sip:ref:`~PyQt6.QtGui.QMouseEvent`. This makes it possible to enable touch events on existing widgets that do not normally handle :sip:ref:`~PyQt6.QtGui.QTouchEvent`. See below for information on some special considerations needed when doing this.

:sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchBegin` is the first touch event sent to a widget. The :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchBegin` event contains a special accept flag that indicates whether the receiver wants the event. By default, the event is accepted. You should call ignore() if the touch event is not handled by your widget. The :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchBegin` event is propagated up the parent widget chain until a widget accepts it with accept(), or an event filter consumes it. For QGraphicsItems, the :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchBegin` event is propagated to items under the mouse (similar to mouse event propagation for QGraphicsItems).

.. _qtouchevent-touch-point-grouping:

Touch Point Grouping
--------------------

As mentioned above, it is possible that several widgets can be receiving QTouchEvents at the same time. However, Qt makes sure to never send duplicate :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchBegin` events to the same widget, which could theoretically happen during propagation if, for example, the user touched 2 separate widgets in a :sip:ref:`~PyQt6.QtWidgets.QGroupBox` and both widgets ignored the :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchBegin` event.

To avoid this, Qt will group new touch points together using the following rules:

* When the first touch point is detected, the destination widget is determined firstly by the location on screen and secondly by the propagation rules.

* When additional touch points are detected, Qt first looks to see if there are any active touch points on any ancestor or descendent of the widget under the new touch point. If there are, the new touch point is grouped with the first, and the new touch point will be sent in a single :sip:ref:`~PyQt6.QtGui.QTouchEvent` to the widget that handled the first touch point. (The widget under the new touch point will not receive an event).

This makes it possible for sibling widgets to handle touch events independently while making sure that the sequence of QTouchEvents is always correct.

.. _qtouchevent-mouse-events-and-touch-event-synthesizing:

Mouse Events and Touch Event Synthesizing
-----------------------------------------

:sip:ref:`~PyQt6.QtGui.QTouchEvent` delivery is independent from that of :sip:ref:`~PyQt6.QtGui.QMouseEvent`. The application flags :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_SynthesizeTouchForUnhandledMouseEvents` and :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_SynthesizeMouseForUnhandledTouchEvents` can be used to enable or disable automatic synthesizing of touch events to mouse events and mouse events to touch events.

.. _qtouchevent-caveats:

Caveats
-------

* As mentioned above, enabling touch events means multiple widgets can be receiving touch events simultaneously. Combined with the default :sip:ref:`~PyQt6.QtWidgets.QWidget.event` handling for QTouchEvents, this gives you great flexibility in designing touch user interfaces. Be aware of the implications. For example, it is possible that the user is moving a :sip:ref:`~PyQt6.QtWidgets.QSlider` with one finger and pressing a :sip:ref:`~PyQt6.QtWidgets.QPushButton` with another. The signals emitted by these widgets will be interleaved.

* Recursion into the event loop using one of the exec() methods (e.g., :sip:ref:`~PyQt6.QtWidgets.QDialog.exec` or :sip:ref:`~PyQt6.QtWidgets.QMenu.exec`) in a :sip:ref:`~PyQt6.QtGui.QTouchEvent` event handler is not supported. Since there are multiple event recipients, recursion may cause problems, including but not limited to lost events and unexpected infinite recursion.

* QTouchEvents are not affected by a :sip:ref:`~PyQt6.QtWidgets.QWidget.grabMouse` or an :sip:ref:`~PyQt6.QtWidgets.QApplication.activePopupWidget`. The behavior of QTouchEvents is undefined when opening a pop-up or grabbing the mouse while there are more than one active touch points.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QEventPoint`, :sip:ref:`~PyQt6.QtGui.QEventPoint.States`, :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_AcceptTouchEvents`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.acceptTouchEvents`.
