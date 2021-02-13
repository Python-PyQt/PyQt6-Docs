.. sip:class-description::
    :status: todo
    :brief: Event which is sent after a widget is hidden
    :digest: 6869dd7ced5ec9695760643527c98683

The :sip:ref:`~PyQt6.QtGui.QHideEvent` class provides an event which is sent after a widget is hidden.

This event is sent just before :sip:ref:`~PyQt6.QtWidgets.QWidget.hide` returns, and also when a top-level window has been hidden (iconified) by the user.

If spontaneous() is true, the event originated outside the application. In this case, the user hid the window using the window manager controls, either by iconifying the window or by switching to another virtual desktop where the window is not visible. The window will become hidden but not withdrawn. If the window was iconified, :sip:ref:`~PyQt6.QtWidgets.QWidget.isMinimized` returns ``true``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QShowEvent`.
