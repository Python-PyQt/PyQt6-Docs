.. sip:method-description::
    :status: todo
    :pysig: 0bee5ee99a425921db962be70be70688
    :realsig: (QMenu*)
    :digest: c3e3934a52a46f37c4313a914b708bd5

Sets the specified *menu* to be the context menu for the system tray icon.

The menu will pop up when the user requests the context menu for the system tray icon by clicking the mouse button.

On macOS, this is currently converted to a NSMenu, so the aboutToHide() signal is not emitted.

**Note:** The system tray icon does not take ownership of the menu. You must ensure that it is deleted at the appropriate time by, for example, creating the menu with a suitable parent object.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.contextMenu`.
