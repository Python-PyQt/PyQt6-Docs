.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d2296759fc2b8d7b801415c51166fa9b

Schedules a :sip:ref:`~PyQt6.QtCore.QEvent.Type.UpdateRequest` event to be delivered to this window.

The event is delivered in sync with the display vsync on platforms where this is possible. Otherwise, the event is delivered after a delay of 5 ms. The additional time is there to give the event loop a bit of idle time to gather system events, and can be overridden using the QT_QPA_UPDATE_IDLE_TIME environment variable.

When driving animations, this function should be called once after drawing has completed. Calling this function multiple times will result in a single event being delivered to the window.

Subclasses of :sip:ref:`~PyQt6.QtGui.QWindow` should reimplement :sip:ref:`~PyQt6.QtGui.QWindow.event`, intercept the event and call the application's rendering code, then call the base class implementation.

**Note:** The subclass' reimplementation of :sip:ref:`~PyQt6.QtGui.QWindow.event` must invoke the base class implementation, unless it is absolutely sure that the event does not need to be handled by the base class. For example, the default implementation of this function relies on :sip:ref:`~PyQt6.QtCore.QEvent.Type.Timer` events. Filtering them away would therefore break the delivery of the update events.
