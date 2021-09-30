.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a context menu event
    :digest: a896bd5d6b0af2135a5c684c4f3868b6

The :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` class contains parameters that describe a context menu event.

Context menu events are sent to widgets when a user performs an action associated with opening a context menu. The actions required to open context menus vary between platforms; for example, on Windows, pressing the menu button or clicking the right mouse button will cause this event to be sent.

When this event occurs it is customary to show a :sip:ref:`~PyQt6.QtWidgets.QMenu` with a context menu, if this is relevant to the context.
