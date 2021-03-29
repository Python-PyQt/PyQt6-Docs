.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a context menu event
    :digest: be5aa3491165b389173d1aa3c55ef078

The :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` class contains parameters that describe a context menu event.

Context menu events are sent to widgets when a user performs an action associated with opening a context menu. The actions required to open context menus vary between platforms; for example, on Windows, pressing the menu button or clicking the right mouse button will cause this event to be sent.

When this event occurs it is customary to show a :sip:ref:`~PyQt6.QtWidgets.QMenu` with a context menu, if this is relevant to the context.

Context menu events contain a special accept flag that indicates whether the receiver accepted the event. If the event handler does not accept the event then, if possible, whatever triggered the event will be handled as a regular input event.
