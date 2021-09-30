.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: f168f03d3b8a57a9528ec56f7ecae6a5

Shows the widget in full-screen mode.

Calling this function only affects :sip:ref:`~PyQt6.QtWidgets.QWidget.isWindow`.

To return from full-screen mode, call :sip:ref:`~PyQt6.QtWidgets.QWidget.showNormal` or :sip:ref:`~PyQt6.QtWidgets.QWidget.close`.

**Note:** Full-screen mode works fine under Windows, but has certain problems under X. These problems are due to limitations of the ICCCM protocol that specifies the communication between X11 clients and the window manager. ICCCM simply does not understand the concept of non-decorated full-screen windows. Therefore, the best we can do is to request a borderless window and place and resize it to fill the entire screen. Depending on the window manager, this may or may not work. The borderless window is requested using MOTIF hints, which are at least partially supported by virtually all modern window managers.

An alternative would be to bypass the window manager entirely and create a window with the :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.X11BypassWindowManagerHint` flag. This has other severe problems though, like totally broken keyboard focus and very strange effects on desktop changes or when the user raises other windows.

X11 window managers that follow modern post-ICCCM specifications support full-screen mode properly.

On macOS, showing a window full screen puts the entire application in full-screen mode, providing it with a dedicated desktop. Showing another window while the application runs in full-screen mode might automatically make that window full screen as well. To prevent that, exit full-screen mode by calling :sip:ref:`~PyQt6.QtWidgets.QWidget.showNormal` or by :sip:ref:`~PyQt6.QtWidgets.QWidget.close` on the full screen window before showing another window.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.showNormal`, :sip:ref:`~PyQt6.QtWidgets.QWidget.showMaximized`, :sip:ref:`~PyQt6.QtWidgets.QWidget.show`, :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible`, :sip:ref:`~PyQt6.QtWidgets.QWidget.close`.
