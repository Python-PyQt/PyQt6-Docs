.. sip:enum-description::
    :status: todo
    :digest: 848f97669a0334cfd828e88d093e4346

This enum type is used to specify various window-system properties for the widget. They are fairly unusual but necessary in a few cases. Some of these flags depend on whether the underlying window manager supports them.

The main types are

There are also a number of flags which you can use to customize the appearance of top-level windows. These have no effect on other windows:

**Note:** The use of this flag is not recommended in multi-monitor environments. This is because the system will enforce that the window maintains its native size when moving it across screens. This is particularly undesirable when using monitors with different resolutions.

On X11, the result of the flag is dependent on the window manager and its ability to understand Motif and/or NETWM hints. Most existing modern window managers can handle this.

**Note:** If the window manager relies on the frame to interactively manipulate the window, the user can no longer move or resize the window via the window system, but this side effect should not be relied on. To produce a fixed size window that can not be resized, please set :sip:ref:`~PyQt6.QtGui.QWindow.setMinimumSize` and :sip:ref:`~PyQt6.QtGui.QWindow.setMaximumSize` to the same size.

The ``CustomizeWindowHint`` flag is used to enable customization of the window controls. This flag must be set to allow the ``WindowTitleHint``, ``WindowSystemMenuHint``, ``WindowMinimizeButtonHint``, ``WindowMaximizeButtonHint`` and ``WindowCloseButtonHint`` flags to be changed.

**Note:** On X11, this hint will work only in window managers that support _NET_WM_STATE_BELOW atom. If a window always on the bottom has a parent, the parent will also be left on the bottom. This window hint is currently not implemented for macOS.

**Note:** On Windows, this will work only for frameless or full-screen windows.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.windowFlags`, `Window Flags Example <https://doc.qt.io/qt-6/qtwidgets-widgets-windowflags-example.html>`_.
