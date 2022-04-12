.. sip:class-description::
    :status: todo
    :brief: Icon for an application in the system tray
    :digest: cf4395895fd3aec9ddd92013c2b3b830

The :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon` class provides an icon for an application in the system tray.

Modern operating systems usually provide a special area on the desktop, called the *system tray* or *notification area*, where long-running applications can display icons and short messages.

.. image:: ../../../images/system-tray.png

The :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon` class can be used on the following platforms:

* All supported versions of Windows.

* All Linux desktop environments that implement the D-Bus `StatusNotifierItem specification <http://www.freedesktop.org/wiki/Specifications/StatusNotifierItem/StatusNotifierItem>`_, including KDE, Gnome, Xfce, LXQt, and DDE.

* All window managers and independent tray implementations for X11 that implement the `freedesktop.org XEmbed system tray specification <http://standards.freedesktop.org/systemtray-spec/systemtray-spec-0.2.html>`_.

* All supported versions of macOS.

To check whether a system tray is present on the user's desktop, call the :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.isSystemTrayAvailable` static function.

To add a system tray entry, create a :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon` object, call :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.setContextMenu` to provide a context menu for the icon, and call :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.show` to make it visible in the system tray. Status notification messages ("balloon messages") can be displayed at any time using :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.showMessage`.

If the system tray is unavailable when a system tray icon is constructed, but becomes available later, :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon` will automatically add an entry for the application in the system tray if the icon is visible.

The :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.activated` signal is emitted when the user activates the icon.

Only on X11, when a tooltip is requested, the :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon` receives a :sip:ref:`~PyQt6.QtGui.QHelpEvent` of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.ToolTip`. Additionally, the :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon` receives wheel events of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.Wheel`. These are not supported on any other platform.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDesktopServices`, `System Tray Icon Example <https://doc.qt.io/qt-6/qtwidgets-desktop-systray-example.html>`_.
