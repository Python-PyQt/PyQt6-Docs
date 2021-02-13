.. sip:method-description::
    :status: todo
    :pysig: 0bee5ee99a425921db962be70be70688
    :realsig: (QMenu*)
    :digest: 537d0dbb3d76e9e703f1ac9e0d0c6363

Sets the specified *menu* to be the context menu for the system tray icon.

The menu will pop up when the user requests the context menu for the system tray icon by clicking the mouse button.

On macOS, this is currenly converted to a NSMenu, so the aboutToHide() signal is not emitted.

**Note:** The system tray icon does not take ownership of the menu. You must ensure that it is deleted at the appropriate time by, for example, creating the menu with a suitable parent object.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.contextMenu`.
