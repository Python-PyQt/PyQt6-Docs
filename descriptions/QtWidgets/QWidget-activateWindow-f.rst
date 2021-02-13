.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 114c7df21a3fe44af8c6e8dc8ce7728a

Sets the top-level widget containing this widget to be the active window.

An active window is a visible top-level window that has the keyboard input focus.

This function performs the same operation as clicking the mouse on the title bar of a top-level window. On X11, the result depends on the Window Manager. If you want to ensure that the window is stacked on top as well you should also call :sip:ref:`~PyQt6.QtWidgets.QWidget.raise_`. Note that the window must be visible, otherwise  has no effect.

On Windows, if you are calling this when the application is not currently the active one then it will not make it the active window. It will change the color of the taskbar entry to indicate that the window has changed in some way. This is because Microsoft does not allow an application to interrupt what the user is currently doing in another application.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.isActiveWindow`, :sip:ref:`~PyQt6.QtWidgets.QWidget.window`, :sip:ref:`~PyQt6.QtWidgets.QWidget.show`.
