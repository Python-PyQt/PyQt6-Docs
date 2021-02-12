.. sip:enum-description::
    :status: todo
    :realname: Qt::WindowType
    :digest: a8c1b5b8d02cf51c0b63da738a9414fe

This enum type is used to specify various window-system properties for the widget. They are fairly unusual but necessary in a few cases. Some of these flags depend on whether the underlying window manager supports them.

The main types are

Indicates that this widget is the desktop.

There are also a number of flags which you can use to customize the appearance of top-level windows. These have no effect on other windows:

**Note:** The use of this flag is not recommended in multi-monitor environments. This is because the system will enforce that the window maintains its native size when moving it across screens. This is particularly undesirable when using monitors with different resolutions.

The ``CustomizeWindowHint`` flag is used to enable customization of the window controls. This flag must be set to allow the ``WindowTitleHint``, ``WindowSystemMenuHint``, ``WindowMinimizeButtonHint``, ``WindowMaximizeButtonHint`` and ``WindowCloseButtonHint`` flags to be changed.

**Note:** On X11, this hint will work only in window managers that support _NET_WM_STATE_BELOW atom. If a window always on the bottom has a parent, the parent will also be left on the bottom. This window hint is currently not implemented for macOS.

**Note:** On Windows, this will work only for frameless or full-screen windows.

.. seealso:: QWidget::windowFlagsWindow Flags Example.
